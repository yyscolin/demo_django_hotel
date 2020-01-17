let screenPosition = 0

function changeScreenPosition(isLeft) {
  screenPosition += isLeft ? -1 : 1
  if (screenPosition < 0)
    screenPosition = maxPosition - 1
  else if (screenPosition == maxPosition)
    screenPosition = 0

  moveScreen()
}

function moveScreen() {
  let distance = parseFloat($('#posters-screen').css('width')) * -1 * screenPosition
  $('#posters-container').css('left', distance + 'px')
}

$(window).on('resize', moveScreen)

function changeGalleryView(thumbnail) {
  if (thumbnail.hasClass('active')) return

  thumbnail.siblings('.active').removeClass('active')
  thumbnail.addClass('active')

  let src = thumbnail.attr('src').replace('-thumbnail', '')
  let views = thumbnail.parent().siblings('.gallery-view')
  views.each((i) => {
    let view = $(views[i])
    if (view.hasClass('active')) {
      view.removeClass('active')
    } else {
      view.attr('src', src)
      view.addClass('active')
    }
  })

  clearInterval(changeGalleryView_Interval)
  changeGalleryView_Interval = setInterval(changeGalleryView_Tick, 4000)
}

function changeGalleryView_Tick() {
  let activeCard = $('.poster-card')[screenPosition]
  let nextImage = $(activeCard).find('.thumbnails>img.active').next()
  if (!nextImage.length) {
    nextImage = $(activeCard).find('.thumbnails>img')[0]
  }
  changeGalleryView($(nextImage))
}

let changeGalleryView_Interval = setInterval(changeGalleryView_Tick, 4000)