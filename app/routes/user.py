from fastapi import FastAPI, HTTPException
from app import app
import logging
from pydantic import BaseModel
from fastapi import Request
from app.controllers import product_controller
from app.models.products import Product

logger = logging.getLogger(__name__)  # get a logger instance

@app.get("/test")
def read_root():
    # logger.info("here") 
    return {"message": "Hi welcome to test Server!"}

@app.post("/create")
async def create_product_endpoint(request: Request):
    """
    API to create a new product.
    """
    data = await request.json()  # Parse request body as JSON
    product = Product(**data)  # Validate and parse data into a Product model
    response = await product_controller.create_product(product)
    return {"message": "Product created successfully", "product": response}


# 2. POST: Edit an existing product
@app.post("/edit/{product_id}")
async def edit_product_endpoint(product_id: str, request: Request):
    """
    API to edit an existing product.
    """
    data = await request.json()  # Parse request body as JSON
    product = Product(**data)  # Validate and parse data into a Product model
    response = await product_controller.edit_product(product_id, product)
    return {"message": "Product updated successfully", "product": response}


# 3. POST: Delete a product by ID
@app.post("/delete/{product_id}")
async def delete_product_endpoint(product_id: str):
    """
    API to delete a product by ID.
    """
    response = await product_controller.delete_product(product_id)
    return {"message": "Product deleted successfully", "result": response}


# 4. GET: Get all existing products
@app.get("/all")
async def get_all_products_endpoint():
    """
    API to fetch all existing products.
    """
    response = await product_controller.get_all_products()
    return {"products": response}


# 5. POST: Change deployment status
@app.post("/change-deployment/{product_id}")
async def change_deployment_status_endpoint(product_id: str, request: Request):
    """
    API to change deployment status of a product.
    """
    data = await request.json()  # Parse request body as JSON
    deployment_status = data.get("deploymentStatus")  # Extract deploymentStatus from body
    if deployment_status is None:
        raise HTTPException(status_code=400, detail="Missing 'deploymentStatus' field")
    response = await product_controller.change_deployment_status(product_id, deployment_status)
    return {"message": "Deployment status updated successfully", "product": response}