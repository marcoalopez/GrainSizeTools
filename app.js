// Color Pool
// --------------

var COLOR_PALETTES = {
  "greenish": ["#687E00", "#4E451A", "#4C7F1F"],
  "blueish": ["#135574", "#242443", "#22102F"],
  "redish": ["#7A1B15", "#5E0A45", "#632A08"]
};

// A Color Pool maintains arbitrary color palettes
// and assigns them in round robin style.

var ColorPool = function(colors) {
  var keys = _.keys(colors);
  var paletteIndex = 0;
  var palettes = {};
  
  // Initialize color indexes
  _.each(colors, function(c, key, index) {
    palettes[key] = {
      paletteIndex: index,
      colorIndex: 0,
      colors: c
    };
  });
  
  // Get a new color, either from a given group or the just the next available
  function getNext(paletteKey) {
    if (paletteKey) {
      var palette = palettes[paletteKey];
      var color = palette.colors[palette.colorIndex];
      palette.colorIndex = (palette.colorIndex+1) % palette.colors.length;
    } else {
      var palette = palettes[keys[paletteIndex]];
      var color = palette.colors[palette.colorIndex];
      palette.colorIndex = (palette.colorIndex+1) % palette.colors.length;
      paletteIndex = (paletteIndex+1) % keys.length;
    }
    return color;
  }
  
  function reset() {
    _.each(palettes, function(palette, key) {
      palette.colorIndex = 0;
    });
    paletteIndex = 0;
  }
  
  return {
    getNext: getNext,
    reset: reset
  }
};



// Lens.Outline
// ==========================================================================
//
// Takes a surface, which is projected to a minimap

var Outline = function(articleEl, state) {
  var that = this;

  this.articleEl = articleEl;
  this.state = state;

  this.el = document.createElement("div");
  this.$el = $(this.el);
  this.$el.addClass('lens-outline');

  // Mouse event handlers
  // --------

  this.$el.mousedown(function(e) {
    that.mouseDown.call(that, e);
  });

  $(window).mousemove(function(e) {
    that.mouseMove.call(that, e);
  });

  $(window).mouseup(function(e) {
    that.mouseUp.call(that, e);
  });

};

Outline.Prototype = function() {

  // Render Document Outline
  // -------------
  //
  // Renders outline and calculates bounds

  this.render = function() {

    var that = this;
    var totalHeight = 0;

    var fragment = window.document.createDocumentFragment();
    this.visibleArea = $('<div class="visible-area"></div>')[0];
    fragment.appendChild(this.visibleArea);

    // Initial Calculations
    // --------

    var contentHeight = $(this.articleEl).height();
    var panelHeight = $(window).height();

    var factor = (contentHeight / panelHeight);
    this.factor = factor;

    // Content height is smaller as the panel height, we don't need a scrollbar
    if (panelHeight >= contentHeight) {
      this.el.innerHTML = "";
      return this;
    }

    // Render nodes
    // --------

    var nodes = $('.content-node');

    nodes.each(function(node) {
      var dn = $(this);
      var nodeId = dn.attr('id');

      var height = dn.outerHeight(true) / factor;

      // Outline node construction
      var $node = $('<div class="node">')
        .attr({
          id: dn.attr('id')// 'outline_'+node.id,
        })
        .css({
          "position": "absolute",
          "height": height-1,
          "top": totalHeight,
          "background": that.state.colors[nodeId],
          "border-color": that.state.colors[nodeId]
        })
        .addClass('text') // .addClass(node.type)
        // .append('<div class="arrow">');

      if (that.state.bookmarks[nodeId]) {
        $node.addClass('highlighted');
      }

      fragment.appendChild($node[0]);
      totalHeight += height;
    });

    // Init scroll pos
    var scrollTop = $(window).scrollTop();

    that.el.innerHTML = "";
    that.el.appendChild(fragment);
    that.updateVisibleArea(scrollTop);

    return this;
  };


  // Update visible area
  // -------------
  //
  // Should get called from the user when the content area is scrolled

  this.updateVisibleArea = function(scrollTop) {
    var targetWidth = $(window).height() / this.factor;
    $(this.visibleArea).css({
      // TODO: add correction to top: so handle works on lower bound
      "top": scrollTop / this.factor,
      "height": Math.max(targetWidth, 20)
    });
  };



  // Handle Mouse down event
  // -----------------
  //

  this.mouseDown = function(e) {
    this._mouseDown = true;
    // When used within a container we use e.pageX (container must have position: fixed)
    var y = e.clientY;

    if (e.target !== this.visibleArea) {
      // Jump to mousedown position
      this.offset = $(this.visibleArea).height()/2;
      this.mouseMove.call(this, e);
    } else {
      this.offset = y - $(this.visibleArea).position().top;
    }
    e.preventDefault();
    e.stopPropagation();
  };

  // Handle Mouse Up
  // -----------------
  //
  // Mouse lifted, no scroll anymore

  this.mouseUp = function() {
    this._mouseDown = false;
  };

  // Handle Scroll
  // -----------------
  //
  // Handle scroll event
  // .visible-area handle

  this.mouseMove = function(e) {

    if (this._mouseDown) {
      // When used within a container we use e.pageX (container must have position: fixed)
      var y = e.clientY;
      // find offset to visible-area.top
      var scroll = (y - this.offset)*this.factor;
      $(window).scrollTop(scroll);
    }
  };
};

Outline.prototype = new Outline.Prototype();


// Reader App
// ==========================================================================

var Reader = function(articleEl) {
  var that = this;

  this.articleEl = articleEl;
  this.colors = new ColorPool(COLOR_PALETTES);
  
  this.state = {
    colors: {},
    bookmarks: {}
  };

  // Attempt restoring bookmarks from localStorage
  this.restoreBookmarks();

  $(this.articleEl).on('click', '.toggle-bookmark', _.bind(this.toggleBookmark, this));

  $('img').on('load', _.bind(this.rerenderOutline, this));
};


Reader.Prototype = function() {

  this.init = function() {
    var contentNodes = $('.content-node');
    var that = this;

    var color = '#444'; 
    // Assign colors
    contentNodes.each(function(node) {
      var nodeId = $(this).attr('id');

      if ($(this).hasClass('level-2') || $(this).hasClass('publication-info')) {
        color = that.colors.getNext();
      }
      
      that.state.colors[nodeId] = color;
    });
  };

  // Render bookmark bar
  this.renderBookmarkLine = function() {
    // Cleanup
    $('.toggle-bookmark').remove();

    var contentNodes = $('.content-node');
    var that = this;

    contentNodes.each(function(node) {
      var dn = $(this);
      var nodeId = dn.attr('id');
      
      var color = that.state.colors[nodeId];

      var bookmarked = that.state.bookmarks[nodeId];
      if (bookmarked) {
        dn.addClass('bookmarked');
        iconColor = 'white';
      } else {
        dn.removeClass('bookmarked');
        iconColor = color;
      }

      // Attach bookmark handle
      var bookmarkHandleEl = $('<a href="#"><div class="stripe" style="background: '+color+'"></div><i class="fa fa-bookmark" style="color: '+iconColor+'"></i></a>');
      bookmarkHandleEl.addClass('toggle-bookmark');
      dn.append(bookmarkHandleEl);
    });
  };

  this.getTitle = function() {
    return document.title;
  };

  this.addBookmark = function(nodeId) {
    this.state.bookmarks[nodeId] = new Date();
    this.storeBookmarks();
  };

  this.removeBookmark = function(nodeId) {
    delete this.state.bookmarks[nodeId];
    this.storeBookmarks();
  };

  this.storeBookmarks = function() {
    localStorage.setItem(document.title, JSON.stringify(this.state.bookmarks));
    this.renderBookmarkLine();
    this.outline.render();
  };

  this.restoreBookmarks = function() {
    var bookmarks = localStorage.getItem(document.title);
    if (bookmarks) {
      this.state.bookmarks = JSON.parse(bookmarks);
    }
  };


  this.rerenderOutline = function() {
    this.outline.render();
    this.outline.updateVisibleArea($(window).scrollTop());
  };

  this.toggleBookmark = function(e) {
    var nodeId = $(e.currentTarget).closest('.content-node').attr('id');
    var bookmark = this.state.bookmarks[nodeId];

    if (bookmark) {
      this.removeBookmark(nodeId);
    } else {
      this.addBookmark(nodeId);
    }
    
    e.preventDefault();
  };

  this.start = function() {
    var that = this;
    this.init();

    this.renderBookmarkLine();

    this.outline = new Outline(this.articleEl, this.state);
    var outlineEl = this.outline.render().el;

    document.body.appendChild(outlineEl);
    
    $(window).on('scroll', function() {
      var scrollTop = $(window).scrollTop();
      that.outline.updateVisibleArea(scrollTop);
    });

    $(window).resize(function() {
      that.rerenderOutline();
    });
  };
};

Reader.prototype = new Reader.Prototype();
