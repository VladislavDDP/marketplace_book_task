const progress = document.querySelector('.progressbar')

window.addEventListener('scroll', event => {
    let windowScroll = document.body.scrollTop || document.documentElement.scrollTop
    let windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight
    progress.style.width = Math.floor(windowScroll / windowHeight * 100) + '%'
})