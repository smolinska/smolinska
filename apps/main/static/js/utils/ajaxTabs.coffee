"use strict"
window.ajaxTabs = (config)->
  if not config.callbacks
    throw Error('ajaxTabs(config) - should specify callbacks')
  if not config.groups
    config.groups = {}

  self = {
    loading: []
    onReady: ($nav) ->
      $links = $nav.find('a')
      $links.click ->
        if isSpecial($(this))
          getSubpage($(this))
      $current = window.utils.currentNav($links)
      if isSpecial($current)
        getSubpage($current)
    loadAll: ($nav)->
      $nav.find('a').each((idx,elm)->
        $e = $(elm)
        if isSpecial($e)
          getSubpage($e)
      )
  }

  getSubpage = ($tab) ->
    type = getType($tab)
    if type not in self.loading
      self.loading.push(type)
      if type of config.groups
        loadGroup(type)
      else # just one tab
        $placeholder = $($tab.attr('href'))
        loadOne(type, $placeholder)

  loadGroup = (type)->
    for slug in config.groups[type]
      $placeholder = $("##{slug}")
      loadOne(type, $placeholder, {slug: slug})
    return

  loadOne = (type, $placeholder, params = {}) ->
    $.get(window.TAB_URLS[type], params, (data)->
        $placeholder.html(data)
        if type of config.callbacks
          config.callbacks[type]($placeholder)
      )

  getType = ($tab)-> parseInt($tab.attr("data-type"))
  # It's form MenuItem.type.choices
  isSpecial = ($tab)-> $tab.length > 0 and not isNaN(getType($tab)) and getType($tab) != window.TAB_TYPES.STANDARD

  return self
