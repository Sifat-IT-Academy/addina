document.getElementById('editBtn').addEventListener('click', function() {
    // Form elementlarini tahrirlashga ochish
    const inputs = document.querySelectorAll('#profileForm input');
    inputs.forEach(input => {
        input.disabled = false;
    });

    // Tugmalarni ko'rsatish
    document.getElementById('saveBtn').style.display = 'inline-block';
    document.getElementById('editBtn').style.display = 'none';
});

document.getElementById('profileForm').addEventListener('submit', function(event) {
    document.getElementById('familya').disabled = false;
    document.getElementById('ism').disabled = false;
    document.getElementById('tugilganSana').disabled = false;
    document.getElementById('email').disabled = false;
    document.getElementById('telefon').disabled = false;
    // Familiya va ismni olamiz
    const familya = document.getElementById('familya').value;
    const ism = document.getElementById('ism').value;

    // Familiya va ismni h2 da yangilash
    document.getElementById('profileName').innerText = `${ism} ${familya}`;

    // Form elementlarini qayta bloklash
    const inputs = document.querySelectorAll('#profileForm input');
    inputs.forEach(input => {
        input.disabled = true;
    });

    // Tugmalarni qayta o'zgartirish
    document.getElementById('saveBtn').style.display = 'none';
    document.getElementById('editBtn').style.display = 'inline-block';
});
document.getElementById('profileImage').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        document.getElementById('profileImg').src = e.target.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    }
});
