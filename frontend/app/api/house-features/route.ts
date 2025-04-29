import { NextResponse } from "next/server"

export async function POST(request: Request) {
  try {
    
    const houseFeatures = await request.json()

    console.log("Received house features:", houseFeatures)

    
    
    const backendResponse = await fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(houseFeatures),
    })
    
    if (!backendResponse.ok) {
      throw new Error(`Backend API error: ${backendResponse.status}`)
    }
    
    const data = await backendResponse.json()
    

    // Simulate calculated data from the backend
    const calculatedData = {
      estimated_price: Math.round(houseFeatures.sq_meters * 2500 + houseFeatures.rooms * 10000),

    }

    
    return NextResponse.json({
      success: true,
      message: "House features received successfully",
      calculatedData,
    })
  } catch (error) {
    console.error("Error processing house features:", error)
    return NextResponse.json(
      {
        success: false,
        message: error instanceof Error ? error.message : "An unknown error occurred",
      },
      { status: 500 },
    )
  }
}
