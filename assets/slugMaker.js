const title = document.querySelector('input[name=title]');
const slug = document.querySelector('input[name=slug]');
function makeSlug (data) {
    return data.toString()
    .toLowerCase()
    .trim()
    .replace(/&/g, '-and-') // replace & with -and-
    .replace(/[\s\W-]+/g, '-') //replace anything not a text with -
}
title.addEventListener('keyup', (e) => {
    slug.setAttribute('value', makeSlug(title.value))
})