const imageInput = document.getElementById('image-input');
const imagePreview = document.getElementById('image-preview');

imageInput.addEventListener('change', function(event) {
  const file = event.target.files[0];
  
  if (file) {
    const reader = new FileReader();
    
    reader.addEventListener('load', function() {
      const imageUrl = reader.result;
      
      // Display the image preview
      imagePreview.innerHTML = `<img src="${imageUrl}" alt="Uploaded Image">`;
    });
    
    reader.readAsDataURL(file);
  }
});
