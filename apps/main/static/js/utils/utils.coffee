"use strict"
self = {}
self.allImagesLoaded = ($container) ->
  loaded = new $.Deferred()
  #  TODO Count already loaded images
  #      $live = $('<div>').html(data)
  #      totalImgCount = $live.find('img').length
  totalImgCount = $container.find('img').length
  imgCount = totalImgCount
  $('img', $container).on('load', ()->
    imgCount--
    loaded.notify((totalImgCount - imgCount) / totalImgCount)
    if imgCount == 0
      loaded.resolve()
  )
  return loaded.promise()

self.makeProgressBar = ($bar) ->
  $inner = $bar.find('.progress-bar')
  return {
    show: -> $bar.hide().removeClass('hidden').fadeIn().promise()
    step: (p)-> $inner.width("#{p}%"); return
    hide: -> $bar.fadeOut().promise().then(-> $inner.width("0%"))
  }

self.progressImagesLoading = ($container, progressBar, callback)->
  utils.allImagesLoaded($container).progress((p)->
      progressBar.step(p * 100)
    ).done(() ->
      progressBar.hide().then(callback)
    )

self.hoverableDropdowns = ($nav) ->
  if window.screen.availWidth >= 800
    $nav.find('.dropdown').hover(
      ()->
        $drop = $(this)
        if !$drop.hasClass('open')
          $drop.find('a[data-toggle="dropdown"]').dropdown('toggle')
      ()->
        $drop = $(this)
        if $drop.hasClass('open')
          $drop.find('a[data-toggle="dropdown"]').dropdown('toggle')
    )

## CHANGING BG
#TODO: Responsive and prefetching
self.changeBackgroundOnEachTab = ($nav)->
  if window.BG_PATH == undefined
    throw "Backend should provide BG_PATH variable"

  BG_ENDING = "_full_hd.jpg"
  changeBg = (id) -> $("body").css('background-image', "url(#{window.BG_PATH}/bg#{id + BG_ENDING})")
  $nav.find('a').each((id, element) ->
    $(element).click(()-> changeBg(id))
    if ($(element).attr('href') == location.hash)
      changeBg(id)
  )

self.currentNav = ($container)->
  if location.hash != ''
    return $container.filter('a[href="' + location.hash + '"]')
  return $()

window.utils = self