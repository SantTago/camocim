var MenuDropDown=function(){this.element=null;this.element_name=null;this.dd_element=null;this.showing=false;this.hiding_continue=false;this.leave_timeout=null;this.enable=function(){this.unsetSimpleListeners();this.setAdvancedListeners();}
this.disable=function(){this.unsetAdvancedListeners();this.clearLeaveTimeout();this.clearOutListeners();this.element.removeClass("showing fade-out");this.showing=false;this.hiding_continue=false;this.setSimpleListeners();}
this.show=function(){this.showing=true;this.element.addClass("showing");}
this.hideInit=function(){this.hiding_continue=true;this.element.removeClass("showing").addClass("fade-out");setTimeout(this.hideComplete.bind(this),300);}
this.hideComplete=function(){if(this.hiding_continue){this.showing=false;this.element.removeClass("fade-out");}else{this.hideCancel();}}
this.hideCancel=function(){this.element.removeClass("fade-out").addClass("showing");this.show();}
this.setLeaveTimeout=function(){if(this.leave_timeout){this.clearLeaveTimeout();}
this.leave_timeout=setTimeout(function(){this.hideInit();this.clearOutListeners();}.bind(this),800);}
this.clearLeaveTimeout=function(){if(this.leave_timeout){clearTimeout(this.leave_timeout);this.leave_timeout=null;}}
this.clearOutListeners=function(){this.element.off("mouseleave");$(document).off("click");}
this.setOutListeners=function(){$(document).on("click",function(e){if($(e.target)[0]==this.element[0]){}else{var p=$(e.target).parent(this.element_name);if(p.length>0&&p[0]==this.element[0]){}else{this.clearLeaveTimeout();this.hideInit();this.clearOutListeners();}}}.bind(this));this.element.on("mouseleave",function(e){this.setLeaveTimeout();}.bind(this));}
this.unsetSimpleListeners=function(){this.element.off("click");}
this.setSimpleListeners=function(){this.element.on("click",function(){if(this.element.hasClass("expanded")){this.element.removeClass("expanded");}else{this.element.addClass("expanded");}}.bind(this));}
this.unsetAdvancedListeners=function(){this.element.off("click");this.element.off("mouseenter");}
this.setAdvancedListeners=function(){this.element.on("click",function(e){e.stopPropagation();if(this.showing){}else{this.show();this.setOutListeners();}}.bind(this));this.element.on("mouseenter",function(e){this.hiding_continue=false;this.clearLeaveTimeout();this.show();this.setOutListeners();}.bind(this));}
this.init=function(element){this.element_name=element;this.element=$(element);this.dd_element=this.element.find(".drop-down-content");this.setAdvancedListeners();return this;}}
var Menu=function(){this.el=null;this.trigger=null;this.open=false;this.dropdownlist=[];this.showMenu=function(){console.log("showMenu");this.open=true;this.trigger.attr("class","animate-in");this.el.show();this.el.attr("class","animate-in");}
this.hideMenu=function(){console.log("hideMenu");this.open=false;this.trigger.attr("class","animate-out");this.el.attr("class","");setTimeout(function(){this.el.hide();}.bind(this),200);}
this.resize=function(){if(window.matchMedia('(max-width: 750px)').matches){this.disableDropdowns();if(this.open){this.el.show();}else{this.el.hide();}}else{this.enableDropdowns();this.el.show();}}
this.disableDropdowns=function(){for(var i=0;i<this.dropdownlist.length;i++){this.dropdownlist[i].disable();}}
this.enableDropdowns=function(){for(var i=0;i<this.dropdownlist.length;i++){this.dropdownlist[i].enable();}}
this.initDropdowns=function(element_name){var dd=$(element_name+" .drop-down");for(var i=0;i<dd.length;i++){this.dropdownlist.push(new MenuDropDown().init(dd[i]));}}
this.initListeners=function(){this.trigger.on("click",function(){if(this.open){this.hideMenu();}else{this.showMenu()}}.bind(this));}
this.init=function(element,trigger){this.el=$(element);this.trigger=$(trigger);this.initDropdowns(element);this.resize();this.initListeners();return this;}}