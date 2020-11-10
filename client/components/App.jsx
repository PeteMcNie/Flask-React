import * as React from 'react'
import { useDispatch } from 'react-redux'
import { useForm } from 'react-hook-form'

import { formAction } from '../actions'

const App = () => {
  const dispatch = useDispatch()
  const { register, handleSubmit, errors } = useForm()

  const onSubmit = data => {
    // console.log(data)
    dispatch(formAction(data))
  }
  console.log(errors)

  return (
    <div>
      <h1>React Form</h1>

      <form onSubmit={handleSubmit(onSubmit)}>
        <label htmlFor='playername'>Name:</label>
        <input id='playername'
          name='playername'
          type="text"
          ref={register({ required: true, maxLength: 80 })} />
        <label htmlFor='password'>Password:</label>

        <input id='password'
          name='password'
          type="text"
          ref={register({ required: true, maxLength: 100 })} />
        <input type='submit' value='Register' />
      </form>

      <p>This current person details are: </p>
    </div>
  )
}

export default App
