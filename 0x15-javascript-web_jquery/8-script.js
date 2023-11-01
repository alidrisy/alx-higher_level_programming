// fetches and lists the title for all movies by using the URL
$.ajax({
  url: 'https://swapi.co/api/films/?format=json',
  success: function (data) {
    $('UL#list_movies').append(...data.results.forEach((movie) => `<li>${movie.title}</li>`));
  }
});
