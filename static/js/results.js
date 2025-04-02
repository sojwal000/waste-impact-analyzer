document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const resultImage = document.getElementById('result-image');
    const wasteType = document.getElementById('waste-type');
    const detectedItemsList = document.getElementById('detected-items-list');
    const confidenceBar = document.getElementById('confidence-bar');
    const confidenceValue = document.getElementById('confidence-value');
    const decompositionTime = document.getElementById('decomposition-time');
    const co2Emissions = document.getElementById('co2-emissions');
    const energyConsumption = document.getElementById('energy-consumption');
    const toxicityLevel = document.getElementById('toxicity-level');
    const microplasticGeneration = document.getElementById('microplastic-generation');
    const disposalCost = document.getElementById('disposal-cost');
    const environmentalHazard = document.getElementById('environmental-hazard');
    const biodegradability = document.getElementById('biodegradability');
    const recommendationsList = document.getElementById('recommendations-list');
    const alternativesList = document.getElementById('alternatives-list');
    const regionSelect = document.getElementById('region-select');
    const regionalGuideline = document.getElementById('regional-guideline');
    const tabButtons = document.querySelectorAll('.tab-btn');
    
    // Get analysis results from session storage
    const resultsData = JSON.parse(sessionStorage.getItem('analysisResults'));
    
    // If no results, redirect to home page
    if (!resultsData) {
        window.location.href = '/';
        return;
    }
    
    // Display results
    displayResults(resultsData);
    
    // Handle tab switching
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons and panes
            tabButtons.forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));
            
            // Add active class to clicked button and corresponding pane
            this.classList.add('active');
            document.getElementById(this.dataset.tab + '-tab').classList.add('active');
        });
    });
    
    // Handle region selection
    regionSelect.addEventListener('change', function() {
        updateRegionalGuidelines(this.value, resultsData.waste_type);
    });
    
    // Function to display results
    function displayResults(data) {
        // Set image
        resultImage.src = data.image_path;
        
        // Set waste type
        wasteType.textContent = data.waste_type;
        
        // Set detected items
        detectedItemsList.innerHTML = '';
        if (data.items && data.items.length > 0) {
            data.items.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item;
                detectedItemsList.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = 'No specific items detected';
            detectedItemsList.appendChild(li);
        }
        
        // Set confidence
        const confidencePercent = Math.round(data.confidence * 100);
        confidenceBar.style.width = confidencePercent + '%';
        
        // Add confidence value inside the bar
        const span = document.createElement('span');
        span.className = 'confidence-value';
        span.textContent = confidencePercent + '%';
        confidenceBar.appendChild(span);
        
        // Set impact data
        decompositionTime.textContent = data.impact.decomposition_time;
        co2Emissions.textContent = data.impact.co2_emissions + ' kg CO₂ per kg';
        energyConsumption.textContent = data.impact.energy_consumption + ' kWh per kg';
        toxicityLevel.textContent = data.impact.toxicity + '/10';
        microplasticGeneration.textContent = data.impact.microplastic_generation;
        disposalCost.textContent = '$' + data.impact.disposal_cost + ' per kg';
        
        // Set environmental hazard with color coding
        environmentalHazard.textContent = data.impact.environmental_hazard;
        if (data.impact.environmental_hazard === 'High') {
            environmentalHazard.style.color = '#d32f2f';
        } else if (data.impact.environmental_hazard === 'Medium') {
            environmentalHazard.style.color = '#ff9800';
        } else {
            environmentalHazard.style.color = '#388e3c';
        }
        biodegradability.textContent = data.impact.biodegradability + '/10';
        
        // Create impact chart
        createImpactChart(data.impact);
        
        // Set recommendations
        recommendationsList.innerHTML = '';
        data.recommendations.forEach(recommendation => {
            const li = document.createElement('li');
            li.textContent = recommendation;
            recommendationsList.appendChild(li);
        });
        
        // Set eco alternatives
        alternativesList.innerHTML = '';
        if (data.impact.eco_alternatives && data.impact.eco_alternatives.length > 0) {
            data.impact.eco_alternatives.forEach(alternative => {
                const li = document.createElement('li');
                li.textContent = alternative;
                alternativesList.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = 'No specific alternatives available';
            alternativesList.appendChild(li);
        }
        
        // Set initial regional guideline
        updateRegionalGuidelines(regionSelect.value, data.waste_type);
    }
    
    // Function to update regional guidelines
    function updateRegionalGuidelines(region, wasteType) {
        const resultsData = JSON.parse(sessionStorage.getItem('analysisResults'));
        if (resultsData && resultsData.impact && resultsData.impact.regional_guidelines) {
            const guidelines = resultsData.impact.regional_guidelines[region];
            if (guidelines) {
                regionalGuideline.textContent = guidelines;
            } else {
                regionalGuideline.textContent = 'No specific guidelines available for this region';
            }
        } else {
            regionalGuideline.textContent = 'No regional guidelines available';
        }
    }
    
    // Function to create impact chart
    function createImpactChart(impactData) {
        const ctx = document.getElementById('impact-chart').getContext('2d');
        
        new Chart(ctx, {
            type: 'radar',
            data: {
                labels: [
                    'CO₂ Emissions',
                    'Water Pollution',
                    'Recyclability',
                    'Landfill Impact',
                    'Toxicity',
                    'Biodegradability'
                ],
                datasets: [{
                    label: 'Environmental Impact',
                    data: [
                        impactData.co2_emissions,
                        impactData.water_pollution,
                        impactData.recyclability,
                        impactData.landfill_impact,
                        impactData.toxicity,
                        impactData.biodegradability
                    ],
                    backgroundColor: 'rgba(76, 175, 80, 0.2)',
                    borderColor: 'rgba(76, 175, 80, 1)',
                    pointBackgroundColor: 'rgba(76, 175, 80, 1)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgba(76, 175, 80, 1)'
                }]
            },
            options: {
                scales: {
                    r: {
                        angleLines: {
                            display: true
                        },
                        suggestedMin: 0,
                        suggestedMax: 10
                    }
                }
            }
        });
    }
});