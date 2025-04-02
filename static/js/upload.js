document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const dropArea = document.getElementById('drop-area');
    const fileInput = document.getElementById('file-input');
    const browseBtn = document.getElementById('browse-btn');
    const previewContainer = document.getElementById('preview-container');
    const previewImage = document.getElementById('preview-image');
    const changeImageBtn = document.getElementById('change-image-btn');
    const analyzeBtn = document.getElementById('analyze-btn');
    const loadingContainer = document.getElementById('loading-container');
    const errorMessage = document.getElementById('error-message');
    
    // Add event listeners for drag and drop
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
    });
    
    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });
    
    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });
    
    function highlight() {
        dropArea.classList.add('highlight');
    }
    
    function unhighlight() {
        dropArea.classList.remove('highlight');
    }
    
    // Handle file drop
    dropArea.addEventListener('drop', handleDrop, false);
    
    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if (files.length) {
            handleFiles(files);
        }
    }
    
    // Handle file selection via browse button
    browseBtn.addEventListener('click', function() {
        fileInput.click();
    });
    
    fileInput.addEventListener('change', function() {
        if (this.files.length) {
            handleFiles(this.files);
        }
    });
    
    // Handle selected files
    function handleFiles(files) {
        const file = files[0];
        
        // Check if file is an image
        if (!file.type.match('image.*')) {
            showError('Please select an image file (JPEG, PNG, GIF).');
            return;
        }
        
        // Check file size (max 5MB)
        if (file.size > 5 * 1024 * 1024) {
            showError('File size exceeds 5MB limit.');
            return;
        }
        
        // Preview the image
        const reader = new FileReader();
        reader.onload = function(e) {
            previewImage.src = e.target.result;
            dropArea.querySelector('form').hidden = true;
            previewContainer.hidden = false;
        };
        reader.readAsDataURL(file);
    }
    
    // Handle change image button
    changeImageBtn.addEventListener('click', function() {
        previewContainer.hidden = true;
        dropArea.querySelector('form').hidden = false;
        fileInput.value = '';
    });
    
    // Handle analyze button
    analyzeBtn.addEventListener('click', function() {
        if (!fileInput.files.length) {
            showError('Please select an image to analyze.');
            return;
        }
        
        // Show loading spinner
        previewContainer.hidden = true;
        loadingContainer.hidden = false;
        errorMessage.hidden = true;
        
        // Create form data
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        
        // Send request to server
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.error || 'Something went wrong');
                });
            }
            return response.json();
        })
        .then(data => {
            // Store results in session storage
            sessionStorage.setItem('analysisResults', JSON.stringify(data));
            
            // Redirect to results page
            window.location.href = '/results';
        })
        .catch(error => {
            loadingContainer.hidden = true;
            previewContainer.hidden = false;
            showError(error.message);
        });
    });
    
    // Show error message
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.hidden = false;
    }
});