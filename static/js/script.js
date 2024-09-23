document.getElementById('editBtn').addEventListener('click', function() {
    // 
    const inputs = document.querySelectorAll('#profileForm input');
    inputs.forEach(input => {
        input.disabled = false;
    });

    // 
    document.getElementById('saveBtn').style.display = 'inline-block';
    document.getElementById('editBtn').style.display = 'none';
});

document.getElementById('profileForm').addEventListener('submit', function(event) {
    event.preventDefault();
    

    const familya = document.getElementById('familya').value;
    const ism = document.getElementById('ism').value;

 
    document.getElementById('profileName').innerText = `${ism} ${familya}`;

    
    const inputs = document.querySelectorAll('#profileForm input');
    inputs.forEach(input => {
        input.disabled = true;
    });

    document.getElementById('saveBtn').style.display = 'none';
    document.getElementById('editBtn').style.display = 'inline-block';

});
// document.getElementById('uploadBtn').addEventListener('click', function() {
//     document.getElementById('imageUpload').click();
// });

// document.getElementById('imageUpload').addEventListener('change', function(event) {
//     const file = event.target.files[0];
    
//     if (file) {
//         const reader = new FileReader();
//         reader.onload = function(e) {
//             document.getElementById('profileImage').src = e.target.result;
//         };
//         reader.readAsDataURL(file); 
//     }
// });