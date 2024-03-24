var cursor = document.querySelector("#cursor")
var cursorBlur = document.querySelector("#cursor-blur")

document.addEventListener("mousemove", function(dets) {
    cursor.style.left = dets.x+"px"
    cursor.style.top = dets.y+"px"
    cursorBlur.style.left = dets.x-250+"px"
    cursorBlur.style.top = dets.y-250+"px"

})

gsap.to("#nav", {
    backgroundColor: "#000",
    duration:0.5,
    height:"110px",
    scrollTrigger:{
        trigger:"#nav",
        scroller: "body",
        start:"top -10%",
        end:"top -11%",
        scrub: 0.5
    }
})

gsap.to("#main",{
    backgroundColor: "#000",
    scrollTrigger:{
        trigger:"#main",
        scroller:"body",
        // markers:true,
        start: "top -30%",
        end: "top -100%",
        scrub: 2
    }
})