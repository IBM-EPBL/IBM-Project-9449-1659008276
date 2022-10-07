window.addEventListener('load', () => {
    const params = (new URL(document.location)).searchParams;
    const name = params.get('name');
    const qualification = params.get('qualification');
    const age = params.get('age');
    const mail = params.get('mail');

    document.getElementById('2nd-name').innerHTML = name;
    document.getElementById('2nd-qualification').innerHTML = qualification;
    document.getElementById('2nd-age').innerHTML = age;
    document.getElementById('2nd-mail').innerHTML = mail;
})