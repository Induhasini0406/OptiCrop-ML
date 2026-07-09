// OptiCrop Client-side Logic

document.addEventListener('DOMContentLoaded', function () {
    const predictForm = document.getElementById('predict-form');
    const loadingOverlay = document.getElementById('loading-overlay');
    
    // Bounds mapping for fields
    const validationBounds = {
        'N': { name: 'Nitrogen', min: 0.0, max: 150.0 },
        'P': { name: 'Phosphorus', min: 5.0, max: 150.0 },
        'K': { name: 'Potassium', min: 5.0, max: 210.0 },
        'temperature': { name: 'Temperature', min: 0.0, max: 50.0 },
        'humidity': { name: 'Humidity', min: 10.0, max: 100.0 },
        'ph': { name: 'pH', min: 3.5, max: 9.0 },
        'rainfall': { name: 'Rainfall', min: 20.0, max: 300.0 }
    };

    if (predictForm) {
        predictForm.addEventListener('submit', function (event) {
            let isValid = true;
            
            // Loop through each field to validate
            for (const [fieldId, bounds] of Object.entries(validationBounds)) {
                const inputElement = document.getElementById(fieldId);
                const feedbackElement = document.getElementById(`${fieldId}-feedback`);
                
                if (!inputElement) continue;
                
                const valueStr = inputElement.value.trim();
                
                // Reset states
                inputElement.classList.remove('is-invalid', 'is-valid');
                if (feedbackElement) feedbackElement.textContent = '';

                // Empty check
                if (valueStr === '') {
                    showError(inputElement, feedbackElement, `${bounds.name} is required.`);
                    isValid = false;
                    continue;
                }

                // Numeric check
                const valueNum = parseFloat(valueStr);
                if (isNaN(valueNum)) {
                    showError(inputElement, feedbackElement, `${bounds.name} must be a valid number.`);
                    isValid = false;
                    continue;
                }

                // Range check
                if (valueNum < bounds.min || valueNum > bounds.max) {
                    showError(inputElement, feedbackElement, `${bounds.name} must be between ${bounds.min} and ${bounds.max}.`);
                    isValid = false;
                    continue;
                }

                // Mark as valid if checks pass
                inputElement.classList.add('is-valid');
            }

            if (!isValid) {
                event.preventDefault(); // Stop form submission
                event.stopPropagation();
            } else {
                // Show loading spinner overlay
                if (loadingOverlay) {
                    loadingOverlay.style.display = 'flex';
                }
            }
        });

        // Add real-time input listeners to clear errors on type
        const inputs = predictForm.querySelectorAll('input');
        inputs.forEach(input => {
            input.addEventListener('input', function () {
                input.classList.remove('is-invalid');
                const feedback = document.getElementById(`${input.id}-feedback`);
                if (feedback) feedback.textContent = '';
            });
        });
    }

    // Helper to show invalid feedback
    function showError(inputElement, feedbackElement, message) {
        inputElement.classList.add('is-invalid');
        if (feedbackElement) {
            feedbackElement.textContent = message;
        }
    }
});
