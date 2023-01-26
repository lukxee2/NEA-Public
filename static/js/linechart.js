window.Apex = {
    chart: {
      foreColor: "#000",
      toolbar: {
        show: false
      }
    },
    stroke: {
      width: 3
    },
    dataLabels: {
      enabled: false
    },
    tooltip: {
      theme: "light",
      x: {
        formatter: function (val) {
          return moment(new Date(val)).format("HH:mm:ss");
        }
      }
    },
    yaxis: {
      decimalsInFloat: 2,
      opposite: false,
      labels: {
        offsetX: -10
      }
    }
  };
  
  var trigoStrength = 3;
  var iteration = 11;
  
  function getRandom() {
    var i = iteration;
    return (
      (Math.sin(i / trigoStrength) * (i / trigoStrength) +
        i / trigoStrength +
        1) *
      (trigoStrength * 2)
    );
  }
  
  function getRangeRandom(yrange) {
    return Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
  }
  
  function generateMinuteWiseTimeSeries(baseval, count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
      var x = baseval;
      var y =
        (Math.sin(i / trigoStrength) * (i / trigoStrength) +
          i / trigoStrength +
          1) *
        (trigoStrength * 2);
  
      series.push([x, y]);
      baseval += 300000;
      i++;
    }
    return series;
  }
  
  function getNewData(baseval, yrange) {
    var newTime = baseval + 300000;
    return {
      x: newTime,
      y: Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min
    };
  }
  
  var optionsColumn = {
    chart: {
      height: 250,
      type: "bar",
      animations: {
        enabled: true
      },
      events: {
        animationEnd: function (chartCtx) {
          const newData = chartCtx.w.config.series[0].data.slice();
          newData.shift();
          window.setTimeout(function () {
            chartCtx.updateOptions(
              {
                series: [
                  {
                    data: newData
                  }
                ],
                xaxis: {
                  min: chartCtx.minX,
                  max: chartCtx.maxX
                },
                subtitle: {
                  text:
                    parseInt(getRangeRandom({ min: 1, max: 20 })).toString() + "%"
                }
              },
              false,
              false
            );
          }, 300);
        }
      },
      toolbar: {
        show: false
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      width: 0
    },
    series: [
      {
        name: "Load Average",
        data: generateMinuteWiseTimeSeries(
          new Date("12/12/2016 00:20:00").getTime(),
          12,
          {
            min: 10,
            max: 110
          }
        )
      }
    ],
    title: {
      text: "Load Average",
      align: "left",
      style: {
        fontSize: "12px"
      }
    },
    subtitle: {
      text: "20%",
      floating: true,
      align: "right",
      offsetY: 0,
      style: {
        fontSize: "22px"
      }
    },
    fill: {
      type: "gradient",
      gradient: {
        shade: "dark",
        type: "vertical",
        shadeIntensity: 0.5,
        inverseColors: false,
        opacityFrom: 1,
        opacityTo: 0.8,
        stops: [0, 100]
      }
    },
    xaxis: {
      type: "datetime",
      range: 2700000
    },
    legend: {
      show: true
    }
  };
  
  // var chartColumn = new ApexCharts(
  //   document.querySelector("#columnchart"),
  //   optionsColumn
  // );
  // chartColumn.render();
  
  var optionsLine = {
    chart: {
      height: 350,
      type: "line",
      stacked: true,
      animations: {
        enabled: true,
        easing: "linear",
        dynamicAnimation: {
          speed: 1000
        }
      },
      dropShadow: {
        enabled: false,
        opacity: 0.3,
        blur: 5,
        left: -7,
        top: 22
      },
      events: {
        animationEnd: function (chartCtx) {
          const newData1 = chartCtx.w.config.series[0].data.slice();
          newData1.shift();
          const newData2 = chartCtx.w.config.series[1].data.slice();
          newData2.shift();
          window.setTimeout(function () {
            chartCtx.updateOptions(
              {
                series: [
                  {
                    data: newData1
                  },
                  {
                    data: newData2
                  }
                ],
                subtitle: {
                  text: parseInt(getRandom() * Math.random()).toString()
                }
              },
              false,
              false
            );
          }, 300);
        }
      },
      toolbar: {
        show: false
      },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: "straight",
      width: 5
    },
    grid: {
      padding: {
        left: 0,
        right: 0
      }
    },
    markers: {
      size: 0,
      hover: {
        size: 0
      }
    },
    series: [
      {
        name: "GET",
        data: generateMinuteWiseTimeSeries(
          new Date("12/12/2016 00:20:00").getTime(),
          12,
          {
            min: 30,
            max: 110
          }
        )
      },
      {
        name: "POST",
        data: generateMinuteWiseTimeSeries(
          new Date("12/12/2016 00:20:00").getTime(),
          12,
          {
            min: 30,
            max: 110
          }
        )
      }
    ],
    xaxis: {
      type: "datetime",
      range: 2700000
    },
    title: {
      text: "Requests",
      align: "left",
      style: {
        fontSize: "0px"
      }
    },
    subtitle: {
      text: "20",
      floating: true,
      align: "right",
      offsetY: 0,
      style: {
        fontSize: "22px"
      }
    },
    legend: {
      show: true,
      floating: true,
      horizontalAlign: "left",
      onItemClick: {
        toggleDataSeries: false
      },
      position: "top",
      offsetY: -33,
      offsetX: 60
    }
  };
  
  var chartLine = new ApexCharts(
    document.querySelector("#linechart"),
    optionsLine
  );
  chartLine.render();
  
  window.setInterval(function () {
    iteration++;
  
    chartLine.updateSeries([
      {
        data: [
          ...chartLine.w.config.series[0].data,
          [chartLine.w.globals.maxX + 300000, getRandom()]
        ]
      },
      {
        data: [
          ...chartLine.w.config.series[1].data,
          [chartLine.w.globals.maxX + 300000, getRandom()]
        ]
      }
    ]);
  
  
    var p3Data = getRangeRandom({ min: 10, max: 100 });
    // chartProgress3.updateOptions({
    //   series: [
    //     {
    //       data: [p3Data]
    //     }
    //   ],
    //   subtitle: {
    //     text: p3Data + "%"
    //   }
    // });
  }, 3000);
  