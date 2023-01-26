fetch('/api/get_room_type_data', {
  method: 'GET', // or 'PUT'
  headers: {
      'Content-Type': 'application/json',
  }})
  .then(response => response.json())
  .then(data => {
  //console.log('Success:', data);
  single = data['Single']
  double = data['Double']
  triple = data['Triple']
  quad = data['Quad']
  var options = {
    series: [single, double, triple, quad],
    labels: ['Single', 'Double', 'Triple', 'Quad'],
    chart: {
    type: 'donut',
  },
  responsive: [{
    breakpoint: 200,
    options: {
      chart: {
        width: 75
      },
      legend: {
        position: 'bottom'
      }
    }
  }]
  };

  var chart = new ApexCharts(document.querySelector("#chart"), options);
  chart.render();
  })
  .catch((error) => {
  console.error('Error:', error);
  });


  var options2 = {
    series: [{
    name: 'Sales',
    data: [31, 40, 28, 51, 42, 109, 100]
  }, {
    name: 'Revenue',
    data: [11, 32, 45, 32, 34, 52, 41]
  }],
    chart: {
    height: 350,
    type: 'area'
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    curve: 'smooth'
  },
  xaxis: {
    type: 'datetime',
    categories: ["2018-09-19T00:00:00.000Z", "2018-09-19T01:30:00.000Z", "2018-09-19T02:30:00.000Z", "2018-09-19T03:30:00.000Z", "2018-09-19T04:30:00.000Z", "2018-09-19T05:30:00.000Z", "2018-09-19T06:30:00.000Z"]
  },
  tooltip: {
    x: {
      format: 'dd/MM/yy HH:mm'
    },
  },
  };

  var chart2 = new ApexCharts(document.querySelector("#graph"), options2);
  chart2.render();

  Apex.grid = {
    padding: {
      right: 0,
      left: 0
    }
  }
  
  Apex.dataLabels = {
    enabled: false
  }
  
  var randomizeArray = function (arg) {
    var array = arg.slice();
    var currentIndex = array.length, temporaryValue, randomIndex;
  
    while (0 !== currentIndex) {
  
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
  
      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
  
    return array;
  }
  
  // data for the sparklines that appear below header area
  var sparklineData = [47, 45, 54, 38, 56, 24, 65, 31, 37, 39, 62, 51, 35, 41, 35, 27, 93, 53, 61, 27, 54, 43, 19, 46];


  var spark1 = {
    chart: {
      id: 'sparkline1',
      group: 'sparklines',
      type: 'area',
      sparkline: {
        enabled: true
      },
    },
    stroke: {
      curve: 'straight'
    },
    fill: {
      opacity: 1,
    },
    series: [{
      name: 'Sales',
      data: randomizeArray(sparklineData)
    }],
    labels: [...Array(24).keys()].map(n => `2018-09-0${n+1}`),
    yaxis: {
      min: 0
    },
    xaxis: {
      type: 'datetime',
    },
    colors: ['#DCE6EC'],
    title: {
      text: '£0',
      offsetX: 20,
      style: {
        fontSize: '24px',
        cssClass: 'apexcharts-yaxis-title'
      }
    },
    subtitle: {
      text: 'Sales',
      offsetX: 20,
      style: {
        fontSize: '14px',
        cssClass: 'apexcharts-yaxis-title'
      }
    }
  }
  

  ///new ApexCharts(document.querySelector("#spark1"), spark1).render();
  //new ApexCharts(document.querySelector("#spark2"), spark1).render();
  ///new ApexCharts(document.querySelector("#spark3"), spark1).render();

  var idata = []
  let i = 30
// setInterval(function(){

//   fetch('/api/get_memory_usage', {
//     method: 'GET', // or 'PUT'
//     headers: {
//         'Content-Type': 'application/json',
//     }})
//     .then(response => response.json())
//     .then(data2=> {
//     // if (idata.length == 8) {
//     //   idata.pop();
//     // }
//     idata.push(data2['data'])
//     //console.log('Success:', data2);
//       i++
//     chart5.updateSeries([{
//       name: 'MemoryUsage',
//       labels: [...Array(i).keys()].map(n => `2022-11-0${n+1}`),
//       data: idata
//     }])
//     //chart5.render();
//     //console.log(data2['data'])
//     //console.log(idata.length)
//   });

// }, 1000);

var spark = {
  chart: {
    id: 'sparkline1',
    group: 'sparklines',
    type: 'area',
    sparkline: {
      enabled: true
    },
  },
  stroke: {
    curve: 'straight'
  },
  fill: {
    opacity: 1,
  },
  series: [{
    name: 'MemoryUsage',
    data: idata
  }],
  labels: [...Array(30).keys()].map(n => `2022-11-0${n+1}`),
  yaxis: {
    min: 0
  },
  xaxis: {
    type: 'datetime',
  },
  colors: ['#232E40'],
  title: {
    text: 'Memory Usage',
    offsetX: 20,
    style: {
      fontSize: '24px',
      cssClass: 'apexcharts-yaxis-title'
    }
  },
  subtitle: {
    text: 'Memory (MB)',
    offsetX: 20,
    style: {
      fontSize: '14px',
      cssClass: 'apexcharts-yaxis-title'
    }
  }
}
///var chart5 = new ApexCharts(document.querySelector("#spark2"), spark);
///chart5.render();

var options6 = {
  series: [{
  name: 'Series 1',
  data: [80, 50, 30, 40, 100, 20],
}],
  chart: {
  height: 350,
  type: 'radar',
},
title: {
  text: ' '
},
xaxis: {
  categories: ['January', 'February', 'March', 'April', 'May', 'June']
}
};

var chart6 = new ApexCharts(document.querySelector("#chart6"), options6);
chart6.render();