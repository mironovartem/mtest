var img1 = new Vue({
  el: '#img1',
  data: {
    seen: true
  }
})

var img1_1 = new Vue({
  el: '#img1_1',
  data: {
    seen: false
  }
})

var p1 = new Vue({
  el: '#p1',
  data: {
    seen:false,
    message: '10'
  }
})

var p2 = new Vue({
  el: '#p2',
  data: {
    seen: true
  },
  methods: {
    chek_it1: function (event) {
      // `this` внутри методов указывает на экземпляр Vue
      p1.seen = true,
      img1.seen = false,
      img1_1.seen = true
      // `event` — нативное событие DOM
    //  if (event) {
    //    alert(event.target.tagName)
    //  }
    }
  }
})
