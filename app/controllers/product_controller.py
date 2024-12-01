from fastapi import HTTPException
from bson import ObjectId
from app.database.database_connection import product_collection
from app.models.products import Product

# Helper function to check if an ObjectId is valid
def is_valid_objectid(product_id):
    return ObjectId.is_valid(product_id)


# 1. Create a product
async def create_product(product: Product):
    product_dict = product.dict()
    result = await product_collection.insert_one(product_dict)
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Error creating product")
    product_dict["_id"] = str(result.inserted_id)
    return product_dict


# 2. Edit an existing product
async def edit_product(product_id: str, product: Product):
    if not is_valid_objectid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")
    update_result = await product_collection.update_one(
        {"_id": ObjectId(product_id)}, {"$set": product.dict()}
    )
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    updated_product = await product_collection.find_one({"_id": ObjectId(product_id)})
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    updated_product["_id"] = str(updated_product["_id"])
    return updated_product


# 3. Delete a product by ID
async def delete_product(product_id: str):
    if not is_valid_objectid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")
    delete_result = await product_collection.delete_one({"_id": ObjectId(product_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}


# 4. Get all existing products
async def get_all_products():
    products = []
    async for product in product_collection.find():
        product["_id"] = str(product["_id"])
        products.append(product)
    return products


# 5. Change deployment status
async def change_deployment_status(product_id: str, deploymentStatus: bool):
    if not is_valid_objectid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")
    update_result = await product_collection.update_one(
        {"_id": ObjectId(product_id)}, {"$set": {"deploymentStatus": deploymentStatus}}
    )
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    updated_product = await product_collection.find_one({"_id": ObjectId(product_id)})
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    updated_product["_id"] = str(updated_product["_id"])
    return updated_product
