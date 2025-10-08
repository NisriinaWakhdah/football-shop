function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon =  document.getElementById('toast-icon');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.removeAttribute('style');
    toastComponent.classList.remove(
        'bg-[#59AC77]', 'border-[#59AC77]', 'text-[#064232]',
        'bg-[#E50046]', 'border-[#E50046]', 'text-black-600',
        'bg-[#FFF100]', 'border-[#FFF100]', 'text-black-800',
        'bg-green-50', 'bg-red-50', 'bg-yellow-50'
    );

    if (type === 'success') {
        toastComponent.style.backgroundColor = '#59AC77';
        toastComponent.style.border = '1px solid #59AC77';
        toastComponent.style.color = '#064232';
        toastIcon.innerHTML = `<i class="fa-solid fa-circle-check"></i>`;
    } else if (type === 'error') {
        toastComponent.style.backgroundColor = '#E50046';
        toastComponent.style.border = '1px solid #E50046';
        toastComponent.style.color = '#000000';
        toastIcon.innerHTML = `<i class="fa-solid fa-circle-xmark"></i>`;
    } else {
        toastComponent.style.backgroundColor = '#FFF100';
        toastComponent.style.border = '1px solid #FFF100';
        toastComponent.style.color = '#000000';
        toastIcon.innerHTML = `<i class="fa-solid fa-bell"></i>`;
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}