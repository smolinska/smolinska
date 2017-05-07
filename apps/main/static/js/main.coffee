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
  $nav.stickyTabs()
  $('[data-toggle="popover"]').popover()
)
$(window).load(()->
  window.scrollHandler()
  ajaxTabs.loadAll($nav)
)

