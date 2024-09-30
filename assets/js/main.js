$(function(){var w=window,d=document,e=d.documentElement,g=d.getElementsByTagName('body')[0],x=w.innerWidth||e.clientWidth||g.clientWidth,y=w.innerHeight||e.clientHeight||g.clientHeight
const Cookies2=new Map()
var dateToday=new Date()
var timeToday=pad(dateToday.getHours(),2)+
':'+
pad(dateToday.getMinutes(),2)+
':'+
pad(dateToday.getSeconds(),2)
if(x>575){}
testimonialCarousel($('.home .section-3 .testimonials'))
testimonialCarousel($('.home .section-5 .testimonials'))
testimonialCarousel($('.how-it-works .section-3 .testimonials'))
testimonialCarousel($('.reviews .section-1 .testimonials'))
testimonialCarousel($('.reviews .section-3 .testimonials'))
testimonialCarousel($('.buy-followers .section-3 .testimonials'))
var plans3=$('.buy-followers .section-1 .plans3')
if(plans3.length){plans3.slick({infinite:true,speed:500,cssEase:'ease',dots:false,arrows:false,centerMode:false,centerPadding:'0px',variableWidth:false,slidesToShow:3,rows:0,responsive:[{breakpoint:991,settings:{slidesToShow:1}},{breakpoint:550,settings:{dots:true,arrows:false,slidesToShow:1}}]})}
var closeInTimer=$('#closeInTimer')
if(closeInTimer.length){if(timeToday=='00:00:00'){Cookies2.remove('close-in')
countdownTimer('08:00:00',closeInTimer.find('.timer'),true)}
countdownTimer('08:00:00',closeInTimer.find('.timer'),true)}
var closeInTimer=$('#closeInTimer2')
if(closeInTimer.length){if(timeToday=='00:00:00'){Cookies2.remove('close-in')
countdownTimer('08:00:00',closeInTimer.find('.timer2'),true)}
countdownTimer('08:00:00',closeInTimer.find('.timer2'),true)}
var closeInTimer=$('#closeInTimer3')
if(closeInTimer.length){if(timeToday=='00:00:00'){Cookies2.remove('close-in')
countdownTimer('08:00:00',closeInTimer.find('.timer3'),true)}
countdownTimer('08:00:00',closeInTimer.find('.timer3'),true)}
var closeInTimer=$('#closeInTimer4')
if(closeInTimer.length){if(timeToday=='00:00:00'){Cookies2.remove('close-in')
countdownTimer('08:00:00',closeInTimer.find('.timer4'),true)}
countdownTimer('08:00:00',closeInTimer.find('.timer4'),true)}
var sectionSuccess=$('.section-claim.success')
if(sectionSuccess.length){var comeBackTimer=sectionSuccess.find('#comeBackTimer')
if(comeBackTimer.length){countdownTimer('24:00:00',comeBackTimer.find('.number'))}
if(x>767){var target=sectionSuccess.find('.sf-panel .body')
var btnBuyUpleap=sectionSuccess.find('.btn-buy-upleap')
var txtDidYouKnow=sectionSuccess.find('.did-you-know')
var txtReachOut=sectionSuccess.find('.reach-out')
btnBuyUpleap.detach().appendTo(target)
txtDidYouKnow.detach().appendTo(target)
txtReachOut.detach().appendTo(target)}}
var sectionReceive=$('.section-claim.receive')
if(sectionReceive.length){var queueNumber=sectionReceive.find('#queueNumber')
if(queueNumber.length){countdownQueue(queueNumber.find('.number'))}}
var sectionContact=$('.section-contact')
if(sectionContact.length){$('.contact #contactForm').ebcaptcha()}
function countdownQueue(display){var count=Math.random()*(12-7+1)+7
count=count.toFixed(3)
splitted=count.split('.')
c1=splitted[0]
c2=splitted[1]
setInterval(function(){if(parseInt(c2)>0){--c2}else{c1--
c2=999}
display.text(pad(c1,2)+' '+pad(c2,3))},1000)}
function countdownTimer(start,display,isContinue=false){var hms=start
if(isContinue){if(Cookies2.get('close-in')){hms=Cookies2.get('close-in')}}
var a=hms.split(':')
var timer=+a[0]*60*60+ +a[1]*60+ +a[2]
var hours
var minutes
var seconds
var refreshIntervalId=setInterval(function(){hours=parseInt((timer/3600)%24,10)
minutes=parseInt((timer/60)%60,10)
seconds=parseInt(timer%60,10)
hours=hours<10?'0'+hours:hours
minutes=minutes<10?'0'+minutes:minutes
seconds=seconds<10?'0'+seconds:seconds
var html=hours+':'+minutes+':'+seconds
if(isContinue){Cookies2.set('close-in',html)}
if(timer>0){display.text(html)}
--timer},1000)}
function pad(num,size){var s='000'+num
return s.substr(s.length-size)}
function testimonialCarousel(target){if(target.length){var testimonials=target.find('.item')
target.slick({infinite:true,speed:500,variableWidth:false,cssEase:'ease',rows:0,responsive:[{breakpoint:3000,settings:{dots:false,arrows:true,centerMode:true,centerPadding:'30px'}},{breakpoint:650,settings:{dots:true,arrows:false,slidesToShow:1}}]})
if(testimonials.length){var vHeight
if(testimonials.hasClass('video')){vHeight=testimonials.first().find('.media').height()}
testimonials.each(function(i,obj){if(obj.classList.contains('message')){$(obj).find('.media').css('height',vHeight+'px')}})}}}});(function($){jQuery.fn.ebcaptcha=function(options){var element=this
var captcha=$(this).find('.captcha')
var html='<label class="label"></label><input type="text" class="form-control input-text input" required data-error="Please solve the math problem."/>'
captcha.html(html)
var input=$(this).find('.input')
var label=$(this).find('.label')
$(element).find('button[type=submit]').attr('disabled','disabled')
var randomNr1=0
var randomNr2=0
var totalNr=0
randomNr1=Math.floor(Math.random()*10)
randomNr2=Math.floor(Math.random()*10)
totalNr=randomNr1+randomNr2
var texti=randomNr1+' + '+randomNr2+' = '
$(label).text(texti)
$(input).keyup(function(){var nr=$(this).val()
if(nr==totalNr){$(element).find('button[type=submit]').removeAttr('disabled')}else{$(element).find('button[type=submit]').attr('disabled','disabled')}})
$(document).keypress(function(e){if(e.which==13){if(element.find('button[type=submit]').is(':disabled')===true){e.preventDefault()
return false}}})}})(jQuery)
$('.standard-plans-btn').click(function(e){$('.standard-plans').removeClass('hide-slick')
$('.premium-plans').addClass('hide-slick')
$('.premium-plans-btn').removeClass('selected-plans-btn')
$('.standard-plans-btn').addClass('selected-plans-btn')})
$('.premium-plans-btn').click(function(e){$('.premium-plans').removeClass('hide-slick')
$('.standard-plans').addClass('hide-slick')
$('.standard-plans-btn').removeClass('selected-plans-btn')
$('.premium-plans-btn').addClass('selected-plans-btn')})
function enableLoading(){$('.loadingBackground').removeClass('hidden')
$('.loadingBackground').addClass('show')
$('body').css({margin:'0',height:'100%',overflow:'hidden'})
$('html').css({margin:'0',height:'100%',overflow:'hidden'})}
function disableLoading(){$('.loadingBackground').removeClass('show')
$('.loadingBackground').addClass('hidden')
$('body').css({margin:'unset',height:'unset',overflow:'unset'})
$('html').css({margin:'unset',height:'unset',overflow:'unset'})}
function proceedWithOrder(value=''){enableLoading()
const para=new URLSearchParams()
para.append('username',value)
window.location.href='/order.html?'+para.toString()}
$('.order-button').click(function(e){let val=''
$('.username').each((i,el)=>{const elValue=$(el).val()
if(elValue)val=elValue})
proceedWithOrder(val)})
$('.username').each((i,el)=>{const element=$(el)
element.keypress(function(e){if(e.keyCode===13){e.preventDefault()
proceedWithOrder(element.val())}})})