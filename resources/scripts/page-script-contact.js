if (isFirefox) {
  $('#floating-plus').css('width', '19px')
}

let  isAjaxActive = false

$('form').submit(() => {
  event.preventDefault()
  if (isAjaxActive) return

  isAjaxActive = true
  $('#envelope-wait').addClass('active')
  $('#envelope-top, #envelope-bottom').addClass('active')
  setTimeout(submitForm, 3000)
})

function getFormData() {
  let payload = []
  $('input, textarea').each((i, element) => {
    element = $(element)
    payload.push(element.attr('name') + '=' + element.val())
  })
  payload = payload.join('&')
  return encodeURI(payload)
}

function submitForm() {
  $.ajax({
    url: '/ajax/contact/',
    method: 'POST',
    data: getFormData(),
    success: (data, textStatus, xhr) => displayAjaxResponse(xhr),
    error: displayAjaxResponse
  })
}

function displayAjaxResponse(xhr) {
  if (xhr.status == 200) {
    var className = 'tick'
    var innerHTML = '&#10003;'
  } else {
    var className = 'cross'
    var innerHTML = '&#10005;'
    xhr.responseText = `Error - ${xhr.responseText}`
  }
  $('#envelope-wait').removeClass('active')
  $('#envelope-symbol').addClass(`active ${className}`).html(innerHTML)
  $('#envelope-message').addClass('active').html(xhr.responseText)


  if (xhr.status != 200) {
    setTimeout(() => {
      $('#envelope-top').removeClass('active')
      $('#envelope-bottom').removeClass('active')
      $('#envelope-symbol').removeClass('active')
      $('#envelope-message').removeClass('active')
    }, 3000)
    setTimeout(() => $('#envelope-symbol').removeClass('cross'), 4000)
    setTimeout(() => isAjaxActive = false, 5250)
  }
}