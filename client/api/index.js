import request from 'superagent'

const flaskland = 'http://localhost:3000/hello'

export function formToApi (data) {
  console.log('API ', data)
  return request
    .get(`${flaskland}`)
    .then(res => {
      console.log('API Response ', res.body)
    })
    .then(data => {
      console.log('API DATA ', data)
    })
}
