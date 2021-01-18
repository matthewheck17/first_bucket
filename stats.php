<?php
ob_start();
include 'dbconfigfb.inc.php';
$conn = new mysqli($db_host, $db_user, $db_pass, $db_name);
$TEAM_ACRONYMS = array("atl", "bkn", "bos", "cha", "chi", "cle", "dal", "den", "det", "gs", "hou", "ind", "lac", "lal", "mem", "mia", "mil", "min", "no", "ny", "okc", "orl", "phi", "phx", "por", "sac", "sa", "tor", "utah", "wsh");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First Bucket</title>
    <link rel="stylesheet" href="./css/stats.css">
    <link rel="stylesheet" href="../node_modules/@fortawesome/fontawesome-free/css/all.css">
</head>
<body>
    <div id="master">
        <a id="home-link" href="./home.html"><img src="./imgs/logo.png"/></a>
        <?php 
            echo '<img id="responsive-team-logo" src="https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/' . $TEAM_ACRONYMS[$_GET['team_id']] .'.png&h=100&w=100" alt="Team-Logo"/>'; 
        ?>
        <div id="flex-container">
            <div id="stats" class="flex-item">
                <div id="game-heading">
                    <span id="player-heading" class="heading">Player</span>
                    <span id="vs-heading" class="heading">Vs</span>
                    <span id="first-team-heading" class="heading">Team</span>
                    <span id="first-overall-heading" class="heading">Ovr</span>
                </div>
                <?php
                    $stmt = $conn->prepare("SELECT * FROM games WHERE team_id = ?"); //get each game
                    $stmt->bind_param('i', $_GET['team_id']);
                    $stmt->execute();
                    $result = $stmt->get_result();
                    while($row = $result->fetch_assoc()) {
                        $stmt2 = $conn->prepare("SELECT team_id FROM games WHERE game_id=? AND NOT team_id=?"); //get the opposing team
                        $stmt2->bind_param('ii', $row["game_id"], $_GET['team_id']);
                        $stmt2->execute();
                        $result2 = $stmt2->get_result();
                        $row2 = $result2->fetch_assoc();
                        echo '<div class="game">';
                        echo '<span class= "player-name">' . $row["first_scorer"] . '</span>';
                        echo '<img class="opponent-logo" src="https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/' . $TEAM_ACRONYMS[$row2['team_id']] . '.png&h=50&w=50" alt="Opponent-Logo"/>';
                        echo '<span class="first-team"><i class="fas fa-basketball-ball"></i></span>';
                        if ($row["overall"] == TRUE){
                            echo '<span class="first-overall"><i class="fas fa-basketball-ball"></i></span>';
                        }
                        echo '</div>';
                    }
                ?>
            </div>
            <div id="logo" class="flex-item">
                <div class="shadow-box">
                    <?php 
                        echo '<img id="team-logo" src="https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/' . $TEAM_ACRONYMS[$_GET['team_id']] .'.png&h=200&w=200" alt="Team-Logo"/>'; 
                    ?>
                </div>
            </div>
    </div>
</body>
</html>