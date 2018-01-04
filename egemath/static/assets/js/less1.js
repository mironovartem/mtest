var p1 = new Vue({
  el: '#p1',
  data: {
    seen: true
  }
})

var p2 = new Vue({
  el: '#p2',
  data: {
    seen:false,
    message: '12'
  }
})

var video1 = new Vue({
  el: '#video1',
  data: {
    seen: false
  }
})


var img1 = new Vue({
  el: '#img1',
  data: {
    seen: true
  }
})
var inpt1 = new Vue({
  el: '#inpt1',
  data: {
    seen: true
  }
})


var p3 = new Vue({
  el: '#p3',
  data: {
    seen: true
  },
  methods: {
    chek_it1: function (event) {
      // `this` внутри методов указывает на экземпляр Vue

      this.seen = false,
      p1.seen = false,
      p4.seen = true,
      p2.seen = true,
      inpt1.seen = false,
      img1.seen = false,
      video1.seen = true


      // `event` — нативное событие DOM
    //  if (event) {
    //    alert(event.target.tagName)
    //  }
    }
  }

})

var p4 = new Vue({
  el: '#p4',
  data: {
    seen: false
  },
  methods: {
    chek_it2: function (event) {
      // `this` внутри методов указывает на экземпляр Vue

      this.seen = false,
      p1.seen = false,
      p2.seen = false,
      //p3.seen = false,
      //inpt1.seen = false,
      //img1.seen = false,
      video1.seen = false,
      p5.seen = true,
      p6.seen = false,
      p7.seen = true,
      p8.seen = false,
      inpt2.seen = false,
      img2.seen = true,
      video2.seen = false


      // `event` — нативное событие DOM
    //  if (event) {
    //    alert(event.target.tagName)
    //  }
    }
  }
})


var p5 = new Vue({
  el: '#p5',
  data: {
    seen: false
  }
})

var p6 = new Vue({
  el: '#p6',
  data: {
    seen:false,
    message1: '12'
  }
})

var video2 = new Vue({
  el: '#video2',
  data: {
    seen: false
  }
})


var img2 = new Vue({
  el: '#img2',
  data: {
    seen: false
  }
})
var inpt2 = new Vue({
  el: '#inpt2',
  data: {
    seen: false
  }
})

var p7 = new Vue({
  el: '#p7',
  data: {
    seen: false
  },
  methods: {
    chek_it3: function (event) {
      // `this` внутри методов указывает на экземпляр Vue

      this.seen = false,
      p5.seen = true,
      p6.seen = true,
      p8.seen = true,
      inpt2.seen = false,
      img2.seen = false,
      video2.seen = true


      // `event` — нативное событие DOM
    //  if (event) {
    //    alert(event.target.tagName)
    //  }
    }
  }

})

var p8 = new Vue({
  el: '#p8',
  data: {
    seen: false
  },
  methods: {
    chek_it4: function (event) {
      // `this` внутри методов указывает на экземпляр Vue

      this.seen = false,

      p6.seen = false,
      p7.seen = false,
      inpt2.seen = false,
      img2.seen = false,
      video2.seen = false


      // `event` — нативное событие DOM
    //  if (event) {
    //    alert(event.target.tagName)
    //  }
    }
  }
})
