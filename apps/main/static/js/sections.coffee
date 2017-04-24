collapseNavbar = ->
  if $('.navbar').offset().top > 50
    $('.navbar-fixed-top').addClass 'top-nav-collapse'
  else
    $('.navbar-fixed-top').removeClass 'top-nav-collapse'
  return

$(window).scroll collapseNavbar
$(()->
  $('.navbar .nav li').click(()->
    $(this).siblings().removeClass('active')
    $(this).addClass('active')
    return
  )
)
# jQuery for page scrolling feature - requires jQuery Easing plugin
$ ->
  $('a.page-scroll').bind 'click', (event) ->
    $anchor = $(this)
    $('html, body').stop().animate { scrollTop: $($anchor.attr('href')).offset().top }, 1000, 'swing'
    event.preventDefault()
    return
  return