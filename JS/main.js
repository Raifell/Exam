async function get_weather (name, count) {
    let div = document.querySelector('.weather');

    const res = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${name}&units=metric&appid=87dd437fcdc65dd21695e123c9257cb9`)
    
    if (res.status < 300) {
        const data = await res.json();

        if (!count) {
            div.style = 'border: 2px solid black;'

            const h = document.createElement('h1');
            h.setAttribute("id", "town_name");
            h.innerHTML = data.name
            div.appendChild(h)

            const country = document.createElement('p');
            country.innerHTML = 'country: ' + data.sys['country']
            country.setAttribute("id", "town_country");
            div.appendChild(country)

            const lo_n = document.createElement('p');
            lo_n.innerHTML = 'lon: ' + data.coord['lon']
            lo_n.setAttribute("id", "town_lon");
            div.appendChild(lo_n)

            const le_t = document.createElement('p');
            le_t.innerHTML = 'lat: ' + data.coord['lat']
            le_t.setAttribute("id", "town_let");
            div.appendChild(le_t)

            const temp = document.createElement('p');
            temp.innerHTML = 'temp: ' + data.main['temp']
            temp.setAttribute("id", "town_temp");
            div.appendChild(temp)

            const feels_like = document.createElement('p');
            feels_like.innerHTML = 'feels like: ' + data.main['feels_like']
            feels_like.setAttribute("id", "town_feel");
            div.appendChild(feels_like)

            const speed = document.createElement('p');
            speed.innerHTML = 'wind speed: ' + data.wind['speed']
            speed.setAttribute("id", "town_speed");
            div.appendChild(speed)

            const clouds = document.createElement('p');
            clouds.innerHTML = 'sky: ' + data.weather[0]['description']
            clouds.setAttribute("id", "town_cloud");
            div.appendChild(clouds)
        } else {
            const h = document.querySelector('#town_name');
            h.innerHTML = ''
            h.innerHTML = data.name

            const country = document.querySelector("#town_country")
            country.innerHTML = ''
            country.innerHTML = 'country: ' + data.sys['country']

            const lo_n = document.querySelector("#town_lon")
            lo_n.innerHTML = ''
            lo_n.innerHTML = 'lon: ' + data.coord['lon']

            const le_t = document.querySelector("#town_let")
            le_t.innerHTML = ''
            le_t.innerHTML = 'lat: ' + data.coord['lat']

            const temp = document.querySelector("#town_temp")
            temp.innerHTML = ''
            temp.innerHTML = 'temp: ' + data.main['temp']

            const feels_like = document.querySelector('#town_feel')
            feels_like.innerHTML = ''
            feels_like.innerHTML = 'feels like: ' + data.main['feels_like']

            const speed = document.querySelector('#town_speed')
            speed.innerHTML = ''
            speed.innerHTML = 'wind speed: ' + data.wind['speed']

            const clouds = document.querySelector('#town_cloud')
            clouds.innerHTML = ''
            clouds.innerHTML = 'sky: ' + data.weather[0]['description']
        }
    }
}


let count = 0
const menu = document.querySelector('.left')
menu.addEventListener('click', function(event) {
    const towns_id = ['town_1', 'town_2', 'town_3', 'town_4', 'town_5', 'town_6', 'town_7', 'town_8', 'town_9', 'town_10', 'town_11', 'town_12', ]

    if (towns_id.includes(event.target.id)) {
        get_weather(event.target.innerText, count)
    }
    if (!count) {
        count += 1
    }
})
