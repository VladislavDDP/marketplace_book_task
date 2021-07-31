const progress = document.querySelector('.progressbar')
const progress_bottom = document.querySelector('.progressbar-bottom')

window.addEventListener('scroll', event => {
    let windowScroll = document.body.scrollTop || document.documentElement.scrollTop
    let windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight
    progress.style.width = Math.floor(windowScroll / windowHeight * 100) + '%'
    progress_bottom.style.height = Math.floor(windowScroll / windowHeight * 100) + '%'
})