"use strict"

initGallery = ($placeholder) ->
  $placeholder.find('.gallery').lightGallery({
    thumbnail: true
  });


conf = {callbacks: {}}
conf.callbacks[window.TAB_TYPES.GALLERY] = initGallery
ajaxTabs = window.ajaxTabs(conf)
$nav = undefined
$(()->
  $nav = $('.navbar')
)

$(window).on('load', ()->
  window.scrollHandler()
  ajaxTabs.loadAll($nav)
)

$(window).scroll(()->
  if ($(this).scrollTop() == 0)
    $('a.nav-link').removeClass('active')
)