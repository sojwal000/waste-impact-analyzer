def analyze_impact(waste_type):
    """
    Analyze the environmental impact of the detected waste type
    
    Args:
        waste_type: The type of waste detected
        
    Returns:
        impact_data: Dictionary containing impact metrics
        recommendations: List of recommendations for handling the waste
    """
    # Impact data for different waste types
    impact_data = {
        "Plastic": {
            "decomposition_time": "450 years",
            "co2_emissions": 6.0,  # kg CO2 per kg of waste
            "water_pollution": 8.5,  # scale 1-10
            "recyclability": 7.0,   # scale 1-10
            "landfill_impact": 9.0,  # scale 1-10
            "energy_consumption": 80.0,  # kWh per kg
            "toxicity": 7.5,  # scale 1-10
            "microplastic_generation": "High",
            "disposal_cost": 0.25,  # $ per kg
            "environmental_hazard": "High",
            "biodegradability": 1.0  # scale 1-10
        },
        "Paper": {
            "decomposition_time": "2-6 weeks",
            "co2_emissions": 1.5,
            "water_pollution": 4.0,
            "recyclability": 9.0,
            "landfill_impact": 5.0,
            "energy_consumption": 35.0,
            "toxicity": 2.0,
            "microplastic_generation": "None",
            "disposal_cost": 0.10,
            "environmental_hazard": "Low",
            "biodegradability": 8.5
        },
        "Glass": {
            "decomposition_time": "1 million years",
            "co2_emissions": 0.8,
            "water_pollution": 3.5,
            "recyclability": 10.0,
            "landfill_impact": 6.0,
            "energy_consumption": 15.0,
            "toxicity": 1.5,
            "microplastic_generation": "None",
            "disposal_cost": 0.15,
            "environmental_hazard": "Low",
            "biodegradability": 1.0
        },
        "Metal": {
            "decomposition_time": "50-200 years",
            "co2_emissions": 4.0,
            "water_pollution": 6.0,
            "recyclability": 8.5,
            "landfill_impact": 7.0,
            "energy_consumption": 95.0,
            "toxicity": 6.0,
            "microplastic_generation": "None",
            "disposal_cost": 0.20,
            "environmental_hazard": "Medium",
            "biodegradability": 1.0
        },
        "Organic": {
            "decomposition_time": "2-5 weeks",
            "co2_emissions": 0.5,
            "water_pollution": 2.0,
            "recyclability": 10.0,
            "landfill_impact": 3.0,
            "energy_consumption": 5.0,
            "toxicity": 1.0,
            "microplastic_generation": "None",
            "disposal_cost": 0.05,
            "environmental_hazard": "Low",
            "biodegradability": 10.0
        },
        "Electronic": {
            "decomposition_time": "Forever",
            "co2_emissions": 8.0,
            "water_pollution": 9.0,
            "recyclability": 6.0,
            "landfill_impact": 10.0,
            "energy_consumption": 120.0,
            "toxicity": 9.5,
            "microplastic_generation": "Medium",
            "disposal_cost": 0.50,
            "environmental_hazard": "High",
            "biodegradability": 0.5
        },
        "Hazardous": {
            "decomposition_time": "Varies",
            "co2_emissions": 9.0,
            "water_pollution": 10.0,
            "recyclability": 3.0,
            "landfill_impact": 10.0,
            "energy_consumption": 100.0,
            "toxicity": 10.0,
            "microplastic_generation": "Varies",
            "disposal_cost": 1.20,
            "environmental_hazard": "High",
            "biodegradability": 0.0
        },
        "Mixed": {
            "decomposition_time": "Varies",
            "co2_emissions": 5.0,
            "water_pollution": 7.0,
            "recyclability": 4.0,
            "landfill_impact": 8.0,
            "energy_consumption": 70.0,
            "toxicity": 6.5,
            "microplastic_generation": "Medium",
            "disposal_cost": 0.30,
            "environmental_hazard": "Medium",
            "biodegradability": 3.0
        },
        "Textiles": {
            "decomposition_time": "Up to 200 years",
            "co2_emissions": 5.5,
            "water_pollution": 7.5,
            "recyclability": 6.0,
            "landfill_impact": 7.5,
            "energy_consumption": 65.0,
            "toxicity": 5.0,
            "microplastic_generation": "High for synthetics",
            "disposal_cost": 0.15,
            "environmental_hazard": "Medium",
            "biodegradability": 4.0
        },
        "Medical": {
            "decomposition_time": "Varies (100+ years)",
            "co2_emissions": 7.5,
            "water_pollution": 8.5,
            "recyclability": 2.0,
            "landfill_impact": 9.5,
            "energy_consumption": 90.0,
            "toxicity": 9.0,
            "microplastic_generation": "Medium",
            "disposal_cost": 2.50,
            "environmental_hazard": "High",
            "biodegradability": 1.0
        },
        "Construction": {
            "decomposition_time": "Varies (50-500 years)",
            "co2_emissions": 6.5,
            "water_pollution": 6.0,
            "recyclability": 7.0,
            "landfill_impact": 8.0,
            "energy_consumption": 85.0,
            "toxicity": 6.0,
            "microplastic_generation": "Low",
            "disposal_cost": 0.40,
            "environmental_hazard": "Medium",
            "biodegradability": 2.0
        },
        "Unknown": {
            "decomposition_time": "Unknown",
            "co2_emissions": 5.0,
            "water_pollution": 5.0,
            "recyclability": 5.0,
            "landfill_impact": 5.0,
            "energy_consumption": 50.0,
            "toxicity": 5.0,
            "microplastic_generation": "Unknown",
            "disposal_cost": 0.25,
            "environmental_hazard": "Medium",
            "biodegradability": 5.0
        }
    }
    
    # Recommendations for different waste types
    recommendations = {
        "Plastic": [
            "Reduce single-use plastic consumption",
            "Recycle plastic items properly",
            "Choose biodegradable alternatives when possible",
            "Support plastic bag bans and regulations",
            "Participate in beach or community cleanups",
            "Use reusable water bottles and shopping bags",
            "Avoid products with microbeads",
            "Try bamboo, glass, or stainless steel alternatives",
            "DIY: Reuse plastic containers for storage or planters"
        ],
        "Paper": [
            "Recycle paper products",
            "Use digital alternatives when possible",
            "Choose recycled paper products",
            "Print double-sided",
            "Compost suitable paper items",
            "Opt for tree-free paper made from bamboo or hemp",
            "Reuse gift wrapping and packaging",
            "DIY: Make recycled paper at home",
            "Use cloth napkins instead of paper ones"
        ],
        "Glass": [
            "Recycle glass containers",
            "Reuse glass jars and bottles",
            "Choose glass over plastic when possible",
            "Properly sort colored and clear glass",
            "Be careful with broken glass disposal",
            "Buy products in returnable glass bottles",
            "DIY: Repurpose glass jars as food containers or candle holders",
            "Use glass containers for food storage instead of plastic",
            "Support deposit return systems for glass bottles"
        ],
        "Metal": [
            "Recycle all metal items",
            "Separate different types of metals",
            "Consider the lifecycle of metal products before purchase",
            "Donate usable metal items",
            "Properly dispose of aerosol cans",
            "Choose durable metal products over disposable alternatives",
            "DIY: Repurpose metal cans as planters or organizers",
            "Buy products with minimal metal packaging",
            "Support companies using recycled metals"
        ],
        "Organic": [
            "Compost organic waste",
            "Reduce food waste through meal planning",
            "Use yard waste for mulching",
            "Consider a home composting system",
            "Support community composting initiatives",
            "Create a worm bin for indoor composting",
            "Use food scraps to make vegetable stock",
            "DIY: Create natural dyes from food waste",
            "Donate excess food to reduce waste"
        ],
        "Electronic": [
            "Use e-waste recycling programs",
            "Donate working electronics",
            "Repair instead of replace when possible",
            "Choose energy-efficient devices",
            "Remove batteries before recycling",
            "Buy refurbished electronics when possible",
            "Participate in manufacturer take-back programs",
            "Properly wipe data before disposal",
            "DIY: Repurpose old electronics for creative projects"
        ],
        "Hazardous": [
            "Use community hazardous waste collection services",
            "Never pour chemicals down drains",
            "Store hazardous materials properly",
            "Choose eco-friendly alternatives",
            "Follow local disposal guidelines strictly",
            "Buy only what you need to avoid excess",
            "Use natural cleaning products instead of harsh chemicals",
            "Research proper disposal methods for specific items",
            "Keep hazardous materials in original containers"
        ],
        "Mixed": [
            "Sort waste before disposal",
            "Learn local recycling guidelines",
            "Reduce consumption of mixed-material products",
            "Choose products with simpler packaging",
            "Advocate for better waste management in your community",
            "Support extended producer responsibility policies",
            "Choose products with clear recycling instructions",
            "Avoid products with multiple types of materials",
            "DIY: Separate components before disposal when possible"
        ],
        "Textiles": [
            "Donate usable clothing and textiles",
            "Repair damaged items instead of discarding",
            "Choose natural fibers over synthetics when possible",
            "Support textile recycling programs",
            "Buy second-hand clothing",
            "Wash synthetic clothing in microplastic-catching bags",
            "DIY: Repurpose old clothing into cleaning rags or quilts",
            "Choose quality over quantity for longer-lasting items",
            "Support brands with take-back programs"
        ],
        "Medical": [
            "Use designated medical waste disposal services",
            "Never flush medications down the toilet",
            "Participate in medication take-back programs",
            "Separate sharps in proper containers",
            "Follow healthcare facility guidelines for disposal",
            "Reduce unnecessary medical packaging when possible",
            "Ask healthcare providers about waste reduction options",
            "Use reusable medical supplies when appropriate and safe",
            "Support medical facilities with waste reduction programs"
        ],
        "Construction": [
            "Separate materials for recycling",
            "Donate usable building materials",
            "Choose sustainable building materials",
            "Plan projects to minimize waste",
            "Reuse materials when possible",
            "Support deconstruction instead of demolition",
            "Use recycled building materials",
            "DIY: Repurpose construction waste for other projects",
            "Research local construction waste recycling facilities"
        ],
        "Unknown": [
            "Contact local waste management for guidance",
            "Research proper disposal methods",
            "Consider the precautionary principle",
            "Reduce consumption of similar items",
            "Support improved waste labeling initiatives",
            "Take photos and ask waste management experts",
            "Check manufacturer websites for disposal information",
            "Join community forums to learn from others' experiences",
            "Advocate for clearer waste classification systems"
        ]
    }
    
    # Regional disposal guidelines (simplified example)
    regional_guidelines = {
        "North America": {
            "Plastic": "Check resin codes 1-7 for local recycling acceptance",
            "Paper": "Generally accepted in curbside recycling",
            "Glass": "Often accepted but may require color sorting",
            "Metal": "Aluminum and steel widely accepted",
            "Organic": "Composting programs available in many cities",
            "Electronic": "Many retailers offer take-back programs",
            "Hazardous": "Community collection events or permanent facilities",
            "Textiles": "Donation centers widely available",
            "Medical": "Pharmacy take-back programs for medications",
            "Construction": "Specialized recycling facilities available"
        },
        "Europe": {
            "Plastic": "Extended producer responsibility programs",
            "Paper": "Widely recycled with high recovery rates",
            "Glass": "Bottle deposit schemes in many countries",
            "Metal": "High recycling rates through separate collection",
            "Organic": "Mandatory separate collection in many areas",
            "Electronic": "WEEE Directive requires proper recycling",
            "Hazardous": "Strict regulations for separate collection",
            "Textiles": "Collection bins widely available",
            "Medical": "Pharmacy return systems for medications",
            "Construction": "High recovery targets under EU directives"
        },
        "Asia": {
            "Plastic": "Informal recycling sector plays major role",
            "Paper": "High demand for recycled fiber",
            "Glass": "Variable recycling rates across regions",
            "Metal": "High value items widely collected",
            "Organic": "Composting less common in urban areas",
            "Electronic": "Growing e-waste management systems",
            "Hazardous": "Regulations developing in many countries",
            "Textiles": "Reuse markets well-established",
            "Medical": "Specialized waste management developing",
            "Construction": "Reuse of materials common in some regions"
        }
    }
    
    # Alternative eco-friendly substitutes
    eco_alternatives = {
        "Plastic": [
            "Bamboo products for kitchenware and personal care",
            "Beeswax wraps instead of plastic wrap",
            "Silicone food storage bags",
            "Glass or stainless steel containers",
            "Plant-based bioplastics for necessary disposables"
        ],
        "Paper": [
            "Digital documents and communications",
            "Reusable cloth napkins and towels",
            "Bamboo or recycled toilet paper",
            "Recycled paper products",
            "Tree-free paper made from agricultural waste"
        ],
        "Glass": [
            "Durable, reusable options that last longer",
            "Recycled glass products",
            "Tempered glass for longer lifespan",
            "Returnable bottle systems",
            "Glass with recycled content"
        ],
        "Metal": [
            "Durable products designed for long life",
            "Products made from recycled metals",
            "Stainless steel food containers",
            "Reusable metal straws and utensils",
            "Aluminum products with recycled content"
        ],
        "Electronic": [
            "Energy-efficient devices",
            "Modular electronics designed for repair",
            "Refurbished electronics",
            "Solar-powered options when available",
            "Devices made with recycled materials"
        ],
        "Textiles": [
            "Organic cotton, hemp, or linen clothing",
            "Recycled polyester made from plastic bottles",
            "Tencel or lyocell from sustainable wood pulp",
            "Natural fiber clothing without synthetic blends",
            "Second-hand or vintage clothing"
        ],
        "Construction": [
            "Reclaimed or salvaged building materials",
            "Bamboo flooring and structures",
            "Recycled content building materials",
            "Hempcrete as an alternative to concrete",
            "Sustainably harvested wood products"
        ]
    }
    
    # Get the basic impact data and recommendations
    basic_impact = impact_data.get(waste_type, impact_data["Unknown"])
    basic_recommendations = recommendations.get(waste_type, recommendations["Unknown"])
    
    # Add regional guidelines and eco-alternatives if available
    result_impact = basic_impact.copy()
    
    # Add regional guidelines (simplified - would need user location in real app)
    result_impact["regional_guidelines"] = {
        region: guidelines.get(waste_type, "No specific guidelines available") 
        for region, guidelines in regional_guidelines.items()
    }
    
    # Add eco-alternatives if available for this waste type
    if waste_type in eco_alternatives:
        result_impact["eco_alternatives"] = eco_alternatives[waste_type]
    else:
        result_impact["eco_alternatives"] = ["No specific alternatives available"]
    
    return result_impact, basic_recommendations