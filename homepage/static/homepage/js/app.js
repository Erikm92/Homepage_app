
window.addEventListener('load',()=>
{
    let long;
    let lat;
    let temperaturedescription = document.querySelector(
        ".temperature-description"
    );
    let temperaturedegree = document.querySelector(
        ".temperature-degree"
    );
    let locationtimezone = document.querySelector(
        ".location-timezone"
    );
    let temperaturesection = document.querySelector(
        ".temperature"
    )
    const temperaturespan = document.querySelector(
        ".temperature span"
    );

    if(navigator.geolocation){
    //We have stopped asking for user location
    // navigator.geolocation.getCurrentPosition(position =>{
    //  console.log(position);
            long = -73.94754560000001;
            lat = 40.6011904;

            var proxyUrl = 'https://cors-anywhere.herokuapp.com/',
            api = `https://api.darksky.net/forecast/1e46afa9aa17ec8673b5fc1108686908/${lat},${long}`
        
            fetch(proxyUrl + api)
             .then(response => {
            return response.json();
        })
            
        .then(data => {
            console.table(data);
        
            const{ temperature, summary, icon} = data.currently;
            //Set DOM elements from the API
            temperaturedegree.textContent = Math.floor(temperature);
            temperaturedescription.textContent = summary;
            locationtimezone.textContent = data.timezone;
            //formula for celcius
            let celcius = (temperature - 32) * (5 / 9);
            //set icon
            seticons(icon, document.querySelector(".icon"));
            //change temp to Celcius/Farh
            temperaturesection.addEventListener('click', () =>{
                if(temperaturespan.textContent ==="F"){
                    temperaturespan.textContent ="C";
                    temperaturedegree.textContent = Math.floor(celcius);
                }
                else{
                    temperaturespan.textContent ="F";
                    temperaturedegree.textContent = Math.floor(temperature);

                }
            }
            )
            
        });
           
   //});
}
    

    function seticons(icon,iconID){
        const skycons = new Skycons({color: "white"});
        const currenticon = icon.replace(/-/g, "_").toUpperCase();
        skycons.play();
        return skycons.set(iconID, Skycons[currenticon]);
        // Error was due to refrencing, from skycons -> Skycons (This is a variable from skycons.js)

    }


});