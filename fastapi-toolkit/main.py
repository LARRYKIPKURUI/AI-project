from fastapi import FastAPI, HTTPException

# 1. Initialize the FastAPI application
# We can add metadata like title and description which will automatically 
# show up in the Swagger UI (/docs).
app = FastAPI(
    title="Developer Tech Stack API",
    description="A beginner-friendly API built for the Moringa Capstone project.",
    version="1.0.0"
)

# 2. Create some mock data
# This dictionary acts as our temporary "database" for the API to serve.
my_stack = {
    "frontend": ["React", "HTML/CSS", "JavaScript"],
    "backend": ["Python", "FastAPI", "Flask", "PHP"],
    "infrastructure": ["AWS", "Ubuntu", "Render"]
}

# 3. Root Endpoint
# The @app.get decorator tells FastAPI that any HTTP GET request to the "/" 
# URL path should be handled by the function right below it.
@app.get("/")
def read_root():
    """Welcome endpoint pointing users to the documentation."""
    return {
        "message": "Welcome to the Developer Tech Stack API!",
        "action": "Visit http://127.0.0.1:8000/docs to see the interactive UI."
    }

# 4. Standard GET Endpoint
# Returns the entire my_stack dictionary as a JSON response.
@app.get("/api/v1/stack")
def get_full_stack():
    """Retrieves the complete tech stack data."""
    return {
        "status": "success",
        "data": my_stack
    }

# 5. Dynamic Endpoint with Path Parameters
# The {category} in the URL allows users to ask for specific data.
@app.get("/api/v1/stack/{category}")
def get_stack_category(category: str):
    """
    Retrieves a specific category from the tech stack.
    Valid categories: frontend, backend, infrastructure.
    """
    # Convert the user's input to lowercase to avoid case-sensitivity errors
    category_lower = category.lower()
    
    # Error Handling: Check if the requested category exists in our data
    if category_lower not in my_stack:
        # If it doesn't exist, return a 404 Not Found error
        raise HTTPException(
            status_code=404, 
            detail="Category not found. Try 'frontend', 'backend', or 'infrastructure'."
        )
        
    # If it does exist, return that specific list
    return {
        "status": "success",
        "category": category_lower,
        "tools": my_stack[category_lower]
    }