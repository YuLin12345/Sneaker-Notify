<!-- Sneaker Notify
 author - Yu Lin
 https://github.com/yulin12345
 admin@yulin12345.site -->
 
<!DOCTYPE html>
<html>
<head>
	<title>W_Notify Database</title>
	<meta charset="utf-8">
<style>
table, th, td{
	border: .7px solid #808080;
}
</style>
</head>
<body>

<p>
<form action="#" method="get">

<!-- Site Selection -->
<select id="site" name="site">
	<option value="EMPTY">Pick a Site</option>
	<option value="addict">Addict</option>
	<option value="adidas">Adidas</option>
	<option value="afew">Afew</option>
	<option value="allike">Allike</option>
	<option value="aphrodite">Aphrodite</option>
	<option value="asphaltgold">Asphaltgold</option>
	<option value="backdoor">Backdoor</option>
	<option value="bait">Bait</option>
	<option value="barneys">Barneys</option>
	<option value="basket">Basket</option>
	<option value="blends">Blends</option>
	<option value="bodega">Bodega</option>
	<option value="bstn">BSTN</option>
	<option value="caliroots">Caliroots</option>
	<option value="capsule">Capsule</option>
	<option value="champs">Champs</option>
	<option value="city">City</option>
	<option value="clicks">Clicks</option>
	<option value="concepts">Concepts</option>
	<option value="consortium">Consortium</option>
	<option value="deadstock">Deadstock</option>
	<option value="defshop">Defshop</option>
	<option value="dopefactory">Dopefactory</option>
	<option value="drome">Drome</option>
	<option value="dsmny">DSMNY</option>
	<option value="eastbay">Eastbay</option>
	<option value="einhalb">43einhalb</option>
	<option value="end">End</option>
	<option value="extrabutter">Extrabutter</option>
	<option value="feature">Feature</option>
	<option value="finishline">Finishline</option>
	<option value="footaction">Footaction</option>
	<option value="footasylum">Footasylum</option>
	<option value="footdistrict">Footdistrict</option>
	<option value="footlocker">Footlocker</option>
	<option value="footlockerEU">Footlockereu</option>
	<option value="footpatrol">Footpatrol</option>
	<option value="footshop">Footshop</option>
	<option value="goodwillout">Goodwillout</option>
	<option value="graffiti">Graffiti</option>
	<option value="hanon">Hanon</option>
	<option value="haven">Haven</option>
	<option value="hhv">HHV</option>
	<option value="holypop">Holypop</option>
	<option value="hubbastille">Hubbastille</option>
	<option value="hypebeast">Hypebeast</option>
	<option value="hypedc">Hypedc</option>
	<option value="inflammable">Inflammable</option>
	<option value="jdsports">JDSports</option>
	<option value="jimmyjazz">Jimmyjazz</option>
	<option value="kicks">Kicks</option>
	<option value="kith">Kith</option>
	<option value="kong">Kong</option>
	<option value="lapstonenhammer">Lapstonenhammer</option>
	<option value="loaded">Loaded</option>
	<option value="luisa">Luisa</option>
	<option value="mrporter">Mrporter</option>
	<option value="needsupply">Needsupply</option>
	<option value="nextdoor">Nextdoor</option>
	<option value="nicekicks">Nicekicks</option>
	<option value="nike">Nike</option>
	<option value="nordstrom">Nordstrom</option>
	<option value="notre">Notre</option>
	<option value="nrml">NRML</option>
	<option value="office">Office</option>
	<option value="offspring">Offspring</option>
	<option value="oneblockdown">Oneblockdown</option>
	<option value="oneness">Oneness</option>
	<option value="overkill">Overkill</option>
	<option value="packer">Packer</option>
	<option value="patta">Patta</option>
	<option value="pointz">Pointz</option>
	<option value="proper">Proper</option>
	<option value="pufferreds">Pufferreds</option>
	<option value="renarts">Renarts</option>
	<option value="rezet">Rezet</option>
	<option value="rise45">Rise45</option>
	<option value="runnerspoint">Runnerspoint</option>
	<option value="ruvilla">Ruvilla</option>
	<option value="saintalfred">Saintalfred</option>
	<option value="saveoursole">Saveoursole</option>
	<option value="shelflife">Shelflife</option>
	<option value="shiekh">Shiekh</option>
	<option value="shoesaddictor">Shoesaddictor</option>
	<option value="shoesgallery">Shoesgallery</option>
	<option value="shoespalace">Shoespalace</option>
	<option value="sidestep">Sidestep</option>
	<option value="size">Size</option>
	<option value="slamjam">Slamjam</option>
	<option value="sneakerbaas">Sneakerbaas</option>
	<option value="sneakerpolitics">Sneakerpolitics</option>
	<option value="sns">SneakerNStuff</option>
	<option value="socialstatus">Socialstatus</option>
	<option value="solebox">Solebox</option>
	<option value="solefly">Solefly</option>
	<option value="solekitchen">Solekitchen</option>
	<option value="solestop">Solestop</option>
	<option value="sportsshoes">Sportsshoes</option>
	<option value="ssense">Ssense</option>
	<option value="stickabush">Stickabush</option>
	<option value="stormfashion">Stormfashion</option>
	<option value="summer">Summer</option>
	<option value="svd">SVD</option>
	<option value="tint">Tint</option>
	<option value="titolo">Titolo</option>
	<option value="tresbien">Tresbien</option>
	<option value="trophyroom">Trophyroom</option>
	<option value="ubiq">Ubiq</option>
	<option value="undefeated">Undefeated</option>
	<option value="uptown">Uptown</option>
	<option value="urbanindustry">Urbanindustry</option>
	<option value="urbanjungle">Urbanjungle</option>
	<option value="urbanoutfitters">Urbanoutfitters</option>
	<option value="wellgosh">Wellgosh</option>
	<option value="westnyc">Westnyc</option>
	<option value="wishatl">Wishatl</option>
	<option value="xileclothing">Xileclothing</option>
	<option value="ycmc">YCMC</option>
	<option value="yeezysupply">Yeezysupply</option>
	<option value="yme">YME</option>
	<option value="zappos">Zappos</option>
</select>

<!-- SortType Selection -->
<select id="sort" name="sort">
	<option value="date">Date</option>
	<option value="name">Name</option>
	<option value="link">Link</option>
</select>

<!-- SortBy Selection -->
<select id="type" name="type">
	<option value="DESC">Descending</option>
	<option value="ASC">Ascending</option>
</select>

<!-- Submit Button -->
<input type="submit" name="form1" value="Submit">
</form>
</p>

<?php

error_reporting(0);

// Connection info.
$servername = " SERVERNAME or HOSTNAME ";
$username = " USERNAME ";
$password = " PASSWORD ";
$dbname = " DBNAME ";

// Make a connection.
$conn = new mysqli($servername, $username, $password, $dbname);

// Check if connection is working.
if($conn->connect_error){
	die("Connection failed " . $conn->connect_error);
}

// Process query.
$sql = "SELECT * FROM " . $_GET["site"] . " ORDER BY " . $_GET["sort"] . " " . $_GET["type"];
$result = $conn->query($sql);

// Get query result.
if($result->num_rows){
	echo "<font size = '3'><table><tr><th>NAME</th><th>LINK</th><th>DATE</th></tr></font size>";
	while($row = $result->fetch_assoc()){
		echo "<tr><td>" . utf8_encode($row["name"]) . "</td><td>" . utf8_encode($row["link"]) . "</td><td>" . utf8_encode($row["date"]) . "</td>";
	}
}
else{
	echo "0 results found.";
}

// Close connection.
$conn->close();
?>


<p>
<form action="#" method="get">

<!-- Site Selection -->
<select id="site" name="site">
	<option value="EMPTY">Pick a Site</option>
	<option value="addict">Addict</option>
	<option value="adidas">Adidas</option>
	<option value="afew">Afew</option>
	<option value="allike">Allike</option>
	<option value="aphrodite">Aphrodite</option>
	<option value="asphaltgold">Asphaltgold</option>
	<option value="backdoor">Backdoor</option>
	<option value="bait">Bait</option>
	<option value="barneys">Barneys</option>
	<option value="basket">Basket</option>
	<option value="blends">Blends</option>
	<option value="bodega">Bodega</option>
	<option value="bstn">BSTN</option>
	<option value="caliroots">Caliroots</option>
	<option value="capsule">Capsule</option>
	<option value="champs">Champs</option>
	<option value="city">City</option>
	<option value="clicks">Clicks</option>
	<option value="concepts">Concepts</option>
	<option value="consortium">Consortium</option>
	<option value="deadstock">Deadstock</option>
	<option value="defshop">Defshop</option>
	<option value="dopefactory">Dopefactory</option>
	<option value="drome">Drome</option>
	<option value="dsmny">DSMNY</option>
	<option value="eastbay">Eastbay</option>
	<option value="einhalb">43einhalb</option>
	<option value="end">End</option>
	<option value="extrabutter">Extrabutter</option>
	<option value="feature">Feature</option>
	<option value="finishline">Finishline</option>
	<option value="footaction">Footaction</option>
	<option value="footasylum">Footasylum</option>
	<option value="footdistrict">Footdistrict</option>
	<option value="footlocker">Footlocker</option>
	<option value="footlockerEU">Footlockereu</option>
	<option value="footpatrol">Footpatrol</option>
	<option value="footshop">Footshop</option>
	<option value="goodwillout">Goodwillout</option>
	<option value="graffiti">Graffiti</option>
	<option value="hanon">Hanon</option>
	<option value="haven">Haven</option>
	<option value="hhv">HHV</option>
	<option value="holypop">Holypop</option>
	<option value="hubbastille">Hubbastille</option>
	<option value="hypebeast">Hypebeast</option>
	<option value="hypedc">Hypedc</option>
	<option value="inflammable">Inflammable</option>
	<option value="jdsports">JDSports</option>
	<option value="jimmyjazz">Jimmyjazz</option>
	<option value="kicks">Kicks</option>
	<option value="kith">Kith</option>
	<option value="kong">Kong</option>
	<option value="lapstonenhammer">Lapstonenhammer</option>
	<option value="loaded">Loaded</option>
	<option value="luisa">Luisa</option>
	<option value="mrporter">Mrporter</option>
	<option value="needsupply">Needsupply</option>
	<option value="nextdoor">Nextdoor</option>
	<option value="nicekicks">Nicekicks</option>
	<option value="nike">Nike</option>
	<option value="nordstrom">Nordstrom</option>
	<option value="notre">Notre</option>
	<option value="nrml">NRML</option>
	<option value="office">Office</option>
	<option value="offspring">Offspring</option>
	<option value="oneblockdown">Oneblockdown</option>
	<option value="oneness">Oneness</option>
	<option value="overkill">Overkill</option>
	<option value="packer">Packer</option>
	<option value="patta">Patta</option>
	<option value="pointz">Pointz</option>
	<option value="proper">Proper</option>
	<option value="pufferreds">Pufferreds</option>
	<option value="renarts">Renarts</option>
	<option value="rezet">Rezet</option>
	<option value="rise45">Rise45</option>
	<option value="runnerspoint">Runnerspoint</option>
	<option value="ruvilla">Ruvilla</option>
	<option value="saintalfred">Saintalfred</option>
	<option value="saveoursole">Saveoursole</option>
	<option value="shelflife">Shelflife</option>
	<option value="shiekh">Shiekh</option>
	<option value="shoesaddictor">Shoesaddictor</option>
	<option value="shoesgallery">Shoesgallery</option>
	<option value="shoespalace">Shoespalace</option>
	<option value="sidestep">Sidestep</option>
	<option value="size">Size</option>
	<option value="slamjam">Slamjam</option>
	<option value="sneakerbaas">Sneakerbaas</option>
	<option value="sneakerpolitics">Sneakerpolitics</option>
	<option value="sns">SneakerNStuff</option>
	<option value="socialstatus">Socialstatus</option>
	<option value="solebox">Solebox</option>
	<option value="solefly">Solefly</option>
	<option value="solekitchen">Solekitchen</option>
	<option value="solestop">Solestop</option>
	<option value="sportsshoes">Sportsshoes</option>
	<option value="ssense">Ssense</option>
	<option value="stickabush">Stickabush</option>
	<option value="stormfashion">Stormfashion</option>
	<option value="summer">Summer</option>
	<option value="svd">SVD</option>
	<option value="tint">Tint</option>
	<option value="titolo">Titolo</option>
	<option value="tresbien">Tresbien</option>
	<option value="trophyroom">Trophyroom</option>
	<option value="ubiq">Ubiq</option>
	<option value="undefeated">Undefeated</option>
	<option value="uptown">Uptown</option>
	<option value="urbanindustry">Urbanindustry</option>
	<option value="urbanjungle">Urbanjungle</option>
	<option value="urbanoutfitters">Urbanoutfitters</option>
	<option value="wellgosh">Wellgosh</option>
	<option value="westnyc">Westnyc</option>
	<option value="wishatl">Wishatl</option>
	<option value="xileclothing">Xileclothing</option>
	<option value="ycmc">YCMC</option>
	<option value="yeezysupply">Yeezysupply</option>
	<option value="yme">YME</option>
	<option value="zappos">Zappos</option>
</select>

<!-- Search Textfield -->
<input type="text" id="search" name="search" placeholder="Keyword" value="">

<!-- Submit Button -->
<input type="submit" name="form2" value="Submit">
</form>
</p>

<?php

error_reporting(0);

// Connection info.
$servername = " SERVERNAME or HOSTNAME ";
$username = " USERNAME ";
$password = " PASSWORD ";
$dbname = " DBNAME ";

// Make a connection.
$conn = new mysqli($servername, $username, $password, $dbname);

// Check if connection is working.
if($conn->connect_error){
	die("Connection failed " . $conn->connect_error);
}

// Process query.
$sql = "SELECT * FROM " . $_GET["site"] . " WHERE name LIKE '%" . $_GET["search"] . "%'";
$result = $conn->query($sql);

// Get query result.
if($result->num_rows){
	echo "<font size = '3'><table><tr><th>NAME</th><th>LINK</th><th>DATE</th></tr></font size>";
	while($row = $result->fetch_assoc()){
		echo "<tr><td>" . utf8_encode($row["name"]) . "</td><td>" . utf8_encode($row["link"]) . "</td><td>" . utf8_encode($row["date"]) . "</td>";
	}
}
else{
	echo "0 results found.";
}

// Close connection.
$conn->close();
?>

</body>
</html>