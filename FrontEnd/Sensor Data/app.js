let activeTab = 5
const gapConfig = [7, 30, 180, 365, 1825, 0]
let myChart

const configChart = (data) => {
    let labels = []
    let voltage = []
    let current = []
    let power = []
    data.map((item) => {
        labels.push(item.date)
        voltage.push({ x: item.date, y: item.voltage })
        current.push({ x: item.date, y: item.current })
        power.push({ x: item.date, y: item.power })
    })

    let ctx = document.getElementById('myChart').getContext('2d');
    console.log(myChart)
    if(myChart){
        myChart.destroy()
    }
    myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Voltage',
                    data: voltage,
                    borderColor: '#6F57E9',
                    backgroundColor: '#B6AAF3',
                },
                {
                    label: 'Current',
                    data: current,
                    borderColor: '#E95D84',
                    backgroundColor: '#F3ADC1',
                },
                {
                    label: 'Power',
                    data: power,
                    borderColor: '#02CCCC',
                    backgroundColor: '#7FE5E5',
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            bezierCurve: true,
            interaction: {
                intersect: false
              },
              plugins: {
                legend: false
              },
            scales: {
                x: {
                    ticks: {
                        callback: function (val, index) {
                            return index % 2 === 0 ? this.getLabelForValue(val) : '';
                        }
                    }
                }
            }
        }
    });
}


const showLoader = () => {
    const loader = document.getElementById('loader')
    loader.style = "display: block;"
}
const hideLoader = () => {
    const loader = document.getElementById('loader')
    loader.style = "display: none;"
}

const fetchSensorLists = () => {
    showLoader()
    axios.get('https://4vxd7h197f.execute-api.us-east-2.amazonaws.com/sensor/list').then((response) => {
        console.log(response)
        let sensorIdDropdown = document.getElementById("sensorIds");
        
        response.data.data.map((item) => {
            let option = document.createElement("option")
            option.textContent = item.sensor_id
            option.value = item.sensor_id
            sensorIdDropdown.appendChild(option)
        })

        hideLoader()
    }).catch((error) => {
        conaole.log(error)
        hideLoader()
    })
}


const chartButtonListener = (childNumber) => {
    activeTab = childNumber
    const childNodes = document.getElementById('buttonPanel').children
    for (let i = 0; i < childNodes.length; i++) {
        childNodes[i].className = ' chartButton'
        if (i === childNumber)
            childNodes[childNumber].className = ' chartButton chartButtonActive'
    }
    let selectedSensorId = document.getElementById("sensorIds").value;
    fetchSensorData(selectedSensorId)
}

selectOnChangeListener = () => {
    let selectedSensorId = document.getElementById("sensorIds").value;
    fetchSensorData(selectedSensorId)
}

fetchSensorData = (selectedSensorId) => {
    showLoader()
    axios.post('https://4vxd7h197f.execute-api.us-east-2.amazonaws.com/readings/get', {
        "sensor_id": selectedSensorId,
        "gap": gapConfig[activeTab]
    }).then((response) => {
        console.log(response)
        configChart(response.data.data)
        hideLoader()
    }).catch((error) => {
        console.log(error)
        hideLoader()

    })
}

fetchSensorLists()