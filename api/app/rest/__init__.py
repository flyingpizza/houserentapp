from fastapi import FastAPI

# Tags for the different routes
tags_metadata = [
    {
        "name": "Model",
        "description": "Operations to get model outputs relating to cold call model.",
    }
]

# Spin up the app
app = FastAPI(
    title="Car Insurance Cold Calling Sales Prediction API",
    description="This is an API to provide predictions from the CarInsurancePredictionModel[TM]",
    version="0.0.1",
    openapi_tags=tags_metadata)


from app.rest.endpoints.calls import router as call_router

app.include_router(call_router)



