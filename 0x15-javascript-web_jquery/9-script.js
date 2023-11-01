// displays the value of hello from that fetch in the HTML tag DIV#hello.
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr',
  function (data) {
    $('DIV#hello').text(data.hello);
  }
);
