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

var p0 = new Vue({
  el: '#p0',
  data: {
    seen:false
  }
})

var p1 = new Vue({
  el: '#p1',
  data: {
    seen:false,
    message: '10'
  }
})

var ob1 = new Vue({
  el: '#ob1',
  data: {
    seen:false
  }
})

var inpt_1 = new Vue({
  el: '#inpt_1',
  data: {
    user_answer_1: '',
    seen: true
  }
})

var p2 = new Vue({
  el: '#p2',
  data: {
    seen: true
  },
  methods: {
    chek_it1: function (event) {
        if (inpt_1.user_answer_1 == '10') {
          p0.seen = true,
          p1.seen = false,
          p2.seen = false,
          img1.seen = true,
          img1_1.seen = false,
          inpt_1.seen = false
       } else {
         p0.seen = false,
         p1.seen = true,
         p2.seen = false,
         img1.seen = false,
         img1_1.seen = true,
         inpt_1.seen = false,
         ob1.seen = true
       }
     }
  }
  })

///////////////////////////////////////

var img2 = new Vue({
  el: '#img2',
  data: {
    seen: true
  }
})

var img2_1 = new Vue({
  el: '#img2_1',
  data: {
    seen: false
  }
})

var p3 = new Vue({
  el: '#p3',
  data: {
    seen:false
  }
})

var p4 = new Vue({
  el: '#p4',
  data: {
    seen:false,
    message2: '8'
  }
})

var ob2 = new Vue({
  el: '#ob2',
  data: {
    seen:false
  }
})

var inpt_2 = new Vue({
  el: '#inpt_2',
  data: {
    user_answer_2: '',
    seen: true
  }
})

var p5 = new Vue({
  el: '#p5',
  data: {
    seen: true
  },
  methods: {
    chek_it2: function (event) {
        if (inpt_2.user_answer_2 == p4.message2) {
          p3.seen = true,
          p4.seen = false,
          p5.seen = false,
          img2.seen = true,
          img2_1.seen = false,
          inpt_2.seen = false
       } else {
         p3.seen = false,
         p4.seen = true,
         p5.seen = false,
         img2.seen = false,
         img2_1.seen = true,
         inpt_2.seen = false,
         ob2.seen = true
       }
     }
  }
  })



  ///////////////////////////////////////

  var img3 = new Vue({
    el: '#img3',
    data: {
      seen: true
    }
  })

  var img3_1 = new Vue({
    el: '#img3_1',
    data: {
      seen: false
    }
  })

  var p6 = new Vue({
    el: '#p6',
    data: {
      seen:false
    }
  })

  var p7 = new Vue({
    el: '#p7',
    data: {
      seen:false,
      message3: '9'
    }
  })

  var ob3 = new Vue({
    el: '#ob3',
    data: {
      seen:false
    }
  })

  var inpt_3 = new Vue({
    el: '#inpt_3',
    data: {
      user_answer_3: '',
      seen: true
    }
  })

  var p8 = new Vue({
    el: '#p8',
    data: {
      seen: true
    },
    methods: {
      chek_it3: function (event) {
          if (inpt_3.user_answer_3 == p7.message3) {
            p6.seen = true,
            p7.seen = false,
            p8.seen = false,
            img3.seen = true,
            img3_1.seen = false,
            inpt_3.seen = false
         } else {
           p6.seen = false,
           p7.seen = true,
           p8.seen = false,
           img3.seen = false,
           img3_1.seen = true,
           inpt_3.seen = false,
           ob3.seen = true
         }
       }
    }
    })



      ///////////////////////////////////////

var img4 = new Vue({
  el: '#img4',
  data: {
    seen: true
  }
})

var img4_1 = new Vue({
  el: '#img4_1',
  data: {
    seen: false
  }
})

var p9 = new Vue({
  el: '#p9',
  data: {
    seen:false
  }
})

var p10 = new Vue({
  el: '#p10',
  data: {
    seen:false,
    message4: '8'
  }
})

var ob4 = new Vue({
  el: '#ob4',
  data: {
    seen:false
  }
})

var inpt_4 = new Vue({
  el: '#inpt_4',
  data: {
    user_answer_4: '',
    seen: true
  }
})

var p11 = new Vue({
  el: '#p11',
  data: {
    seen: true
  },
  methods: {
    chek_it4: function (event) {
        if (inpt_4.user_answer_4 == p10.message4) {
          p9.seen = true,
          p10.seen = false,
          p11.seen = false,
          img4.seen = true,
          img4_1.seen = false,
          inpt_4.seen = false
       } else {
         p9.seen = false,
         p10.seen = true,
         p11.seen = false,
         img4.seen = false,
         img4_1.seen = true,
         inpt_4.seen = false,
         ob4.seen = true
       }
     }
   }
})


///////////////////////////////////////

var img5 = new Vue({
  el: '#img5',
  data: {
    seen: true
  }
})

var img5_1 = new Vue({
  el: '#img5_1',
  data: {
    seen: false
  }
})

var p12 = new Vue({
  el: '#p12',
  data: {
    seen:false
  }
})

var p13 = new Vue({
  el: '#p13',
  data: {
    seen:false,
    message5: '8'
  }
})

var ob5 = new Vue({
  el: '#ob5',
  data: {
    seen:false
  }
})

var inpt_5 = new Vue({
  el: '#inpt_5',
  data: {
    user_answer_5: '',
    seen: true
  }
})

var p14 = new Vue({
  el: '#p14',
  data: {
    seen: true
  },
  methods: {
    chek_it5: function (event) {
      if (inpt_5.user_answer_5 == p13.message5) {
        p12.seen = true,
        p13.seen = false,
        p14.seen = false,
        img5.seen = true,
        img5_1.seen = false,
        inpt_5.seen = false
      } else {
        p12.seen = false,
        p13.seen = true,
        p14.seen = false,
        img5.seen = false,
        img5_1.seen = true,
        inpt_5.seen = false,
        ob5.seen = true
      }
    }
  }
})

///////////////////////////////////////

var img6 = new Vue({
  el: '#img6',
  data: {
    seen: true
  }
})

var img6_1 = new Vue({
  el: '#img6_1',
  data: {
    seen: false
  }
})

var p15 = new Vue({
  el: '#p15',
  data: {
    seen:false
  }
})

var p16 = new Vue({
  el: '#p16',
  data: {
    seen:false,
    message6: '8'
  }
})

var ob6 = new Vue({
  el: '#ob6',
  data: {
    seen:false
  }
})

var inpt_6 = new Vue({
  el: '#inpt_6',
  data: {
    user_answer_6: '',
    seen: true
  }
})

var p17 = new Vue({
  el: '#p17',
  data: {
    seen: true
  },
  methods: {
    chek_it6: function (event) {
      if (inpt_6.user_answer_6 == p16.message6) {
        p15.seen = true,
        p16.seen = false,
        p17.seen = false,
        img6.seen = true,
        img6_1.seen = false,
        inpt_6.seen = false
      } else {
        p15.seen = false,
        p16.seen = true,
        p17.seen = false,
        img6.seen = false,
        img6_1.seen = true,
        inpt_6.seen = false,
        ob6.seen = true
      }
    }
  }
})

///////////////////////////////////////

var img7 = new Vue({
  el: '#img7',
  data: {
    seen: true
  }
})

var img7_1 = new Vue({
  el: '#img7_1',
  data: {
    seen: false
  }
})

var p18 = new Vue({
  el: '#p18',
  data: {
    seen:false
  }
})

var p19 = new Vue({
  el: '#p19',
  data: {
    seen:false,
    message7: '8'
  }
})

var ob7 = new Vue({
  el: '#ob7',
  data: {
    seen:false
  }
})

var inpt_7 = new Vue({
  el: '#inpt_7',
  data: {
    user_answer_7: '',
    seen: true
  }
})

var p20 = new Vue({
  el: '#p20',
  data: {
    seen: true
  },
  methods: {
    chek_it7: function (event) {
      if (inpt_7.user_answer_7 == p19.message7) {
        p18.seen = true,
        p19.seen = false,
        p20.seen = false,
        img7.seen = true,
        img7_1.seen = false,
        inpt_7.seen = false
      } else {
        p18.seen = false,
        p19.seen = true,
        p20.seen = false,
        img7.seen = false,
        img7_1.seen = true,
        inpt_7.seen = false,
        ob7.seen = true
      }
    }
  }
})


///////////////////////////////////////

var img8 = new Vue({
  el: '#img8',
  data: {
    seen: true
  }
})

var img8_1 = new Vue({
  el: '#img8_1',
  data: {
    seen: false
  }
})

var p21 = new Vue({
  el: '#p21',
  data: {
    seen:false
  }
})

var p22 = new Vue({
  el: '#p22',
  data: {
    seen:false,
    message8: '8'
  }
})

var ob8 = new Vue({
  el: '#ob8',
  data: {
    seen:false
  }
})

var inpt_8 = new Vue({
  el: '#inpt_8',
  data: {
    user_answer_8: '',
    seen: true
  }
})

var p23 = new Vue({
  el: '#p23',
  data: {
    seen: true
  },
  methods: {
    chek_it8: function (event) {
      if (inpt_8.user_answer_8 == p22.message8) {
        p21.seen = true,
        p22.seen = false,
        p23.seen = false,
        img8.seen = true,
        img8_1.seen = false,
        inpt_8.seen = false
      } else {
        p21.seen = false,
        p22.seen = true,
        p23.seen = false,
        img8.seen = false,
        img8_1.seen = true,
        inpt_8.seen = false,
        ob8.seen = true
      }
    }
  }
})
