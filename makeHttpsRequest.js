const https = require('https');
/*
 * Complete the function below.
 * Use console.log to print the result, you should not return from the function.
 */
async function getNumberOfMovies(substr) {
    /*
     * Endpoint: "https://jsonmock.hackerrank.com/api/movies/search/?Title=substr"
     */
    const options = {
        host: 'jsonmock.hackerrank.com',
        path: `/api/movies/search/?Title=${substr}`,
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }
    let total;
    const req = https.request(options, res => {
        let string = ''
        
        res.on('data', chunk => string += chunk)
        res.on('end', () => console.log(string[0]));
    });

    req.on('error', err => {
        console.log(err)
    })

    req.end()

    return total;
}

console.log(getNumberOfMovies('maze'))