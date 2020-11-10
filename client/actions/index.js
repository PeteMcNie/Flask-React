import { formToApi } from '../api'

export const SENDING_FORM = 'SENDING_FORM'
export const SENDING_FORM_SUCCESS = 'SENDING_FORM_SUCCESS'

export function formAction (data) {
//   console.log('ACTION ', data)
  return (dispatch) => {
    dispatch(sendingForm())
    return formToApi(data)
  }
}

export function sendingForm () {
  return {
    type: SENDING_FORM
  }
}
