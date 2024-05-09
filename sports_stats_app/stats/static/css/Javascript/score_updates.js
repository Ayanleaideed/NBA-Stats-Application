$(document).ready(function () {
  // Fetch the URL from a data attribute in the HTML
  var fetchUrl = $('#fetch-url').data('url');

  function fetchData() {
    $.ajax({
      url: fetchUrl,
      type: 'GET',
      dataType: 'json',
      success: function (data) {
        if (data.games) {
          data.games.forEach(function (game, index) {
            var scoreCard = $('#score-card-' + index);
            scoreCard.find('.score-header').text(game.home_team + ' vs ' + game.away_team);
            scoreCard.find('.card-body div').eq(0).text('Score: ' + game.home_score + ' - ' + game.away_score);
            scoreCard.find('.card-body div').eq(1).text('Status: ' + game.status);
            scoreCard.find('.card-body div').eq(2).text('Date: ' + game.date);
            scoreCard.find('.card-body div').eq(3).text('Series: ' + game.series_text);
          });
          console.log(data.games);
        }
      },
      error: function (error) {
        console.log('Error:', error);
      }
    });
  }

  setInterval(fetchData, 50000); // Refresh every 10 seconds

  document.addEventListener("DOMContentLoaded", function () {
    const scoreCards = document.querySelectorAll('.score-card');
    const totalWidth = scoreCards.length * 310; // Each card width + margin-right
    const marquee = document.querySelector('.scores-marquee');

    const duration = Math.max(30, scoreCards.length * 3);
    marquee.style.animationDuration = `${duration}s`;

    document.styleSheets[0].insertRule(`
      @keyframes marquee {
        from { transform: translate3d(${window.innerWidth}px, 0, 0); }
        to { transform: translate3d(-${totalWidth}px, 0, 0); }
      }
    `, document.styleSheets[0].cssRules.length);
  });
});
