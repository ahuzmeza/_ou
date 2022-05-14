<!-- Main page -->
<?php include('api/server.php') ?>

<!DOCTYPE html>
<html lang="ro">

<head>
    <title> MyNote - Service </title>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta author="ahuzmeza">
    
    <link rel="stylesheet" type="text/css" href="css/style.css">
    
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>

</head>
<body>
<!-- ================ Menue =================-->
    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="./index.php"> MyNote </a>
            </div>
            <ul class="nav navbar-nav navbar-right">
                <?php  if (isset($_SESSION['username'])) : ?>        
                        <?php include("components/comp_logged_in.php"); ?>
                <? else: ?>
                        <?php include('components/comp_logged_out.php'); ?>    
                <?php endif ?>
            </ul>
        </div>
    </nav>

    <div class="content">
  	<!-- notification message -->
  	<?php if (!isset($_SESSION['success'])) : ?>
        
        <!-- Only if logged in show: -->
        
  	<?php endif ?>
    </div>
    
<!-- ================End  Menu =================-->
<header>
		<div class="hero">
			<div class="hero__canvas">
				<div class="container">
					<div class="roll-text page-header">
						<h2> Salvează<span class="txt-rotate" data-period="2000"
								data-rotate='[ "-ți notițele cu MyNote ", "-ți notițele cu MyNote ! " ]'>
							</span>
						</h2>
					</div>
				</div>
				
                <img src="./vendor/img/forest.jpg" alt="">

                <a href="./components/comp_note_list.php">
				<div class="hero__box text-center hero__link">
					<h1> Notitele mele! </h1>
					<p> Toate notitele tale sunt salvate automat aici.</p>
					<span class="hero__box--right"></span>

				</div>
            </a>
		</div>

		</div>
	</header>

	<section class="about section-margin mb-5">
		<div class="container">
			<div class="row align-items-center">
				<div class="col-md-5">
					<div class="about__img text-center text-md-left mb-5 mb-md-0">
						<a href="#/" class="about__img__date text-center">
                        <?php
                            // get user count from table users from $db
                            $query = "SELECT * FROM users";
                            $result = mysqli_query($db, $query);
                            $user_count = mysqli_num_rows($result);
                            echo "<h2>$user_count</h2>";
                        ?>
							<h3> Users </h3>
						</a>
					</div>
				</div>
				<div class="col-md-7 pl-xl-5">
					<div class="section-intro">
						<h3 class="section-intro__title" style="font-size: 23px;">About This service </h3>
						<h2 class="section-intro__subtitle"> Faset & easy <br> online note taking.</h2>
					</div>
					<p> Create as many notes, every note will be automatically kept upt to date
                        as you write your text.
                    </p>
					<p> You just need to create an account for easy acces to all your notes 
                        anywhere in the world.
                    
                        Notes can be shared between users soon.</p>
					<a class="btn btn-dark mt-4" href="#/">Read More</a>
				</div>
			</div>
		</div>
	</section>

	<section class="overview">
		<div class="container">
			<div class="row">
				<div class="col-sm-8 col-lg-6 col-xl-4 mb-4 mb-xl-0">
					<div class="media align-items-center overview__single">
						<span class="overview__single__icon"><i class="ti-crown"></i></span>
						<div class="media-body">
                        <?php
                            // get all notes from table user_notes from $db
                            $query = "SELECT * FROM user_notes";
                            $result = mysqli_query($db, $query);
                            $note_count = mysqli_num_rows($result);
                            echo "<h2>$note_count</h2>";
                        ?>
							<p>Notes</p>
						</div>
					</div>
				</div>

				<div class="col-sm-8 col-lg-6 col-xl-4 mb-4 mb-xl-0">
					<div class="media align-items-center overview__single">
						<span class="overview__single__icon"><i class="ti-face-smile"></i></span>
						<div class="media-body">
                        <?php  
                            if (isset($_SESSION['username'])) {    
                                $query = "SELECT * FROM user_notes WHERE username_id = '$_SESSION[username]'";
                                $result = mysqli_query($db, $query);
                                $note_count = mysqli_num_rows($result);
                                echo "<h2>$note_count</h2>";
                                echo "<p> Your's </p>";

                            }
                            else {
                                echo "<h2> Login </h2>";
                                echo "<p> to see your note count </p>";
                            }
                        ?>
						</div>
					</div>
				</div>
									
			</div>
		</div>
	</section>

	<footer class="footer footer-bg">
		<div class="container">
			<div class="row">
				<div class="col-sm-4 col-lg-2 mb-4 mb-lg-0 text-left">
					<h3 class="footer__title">About</h3>
					<ul class="footer__link">
						<li><a href="#/"> How it works? e</a></li>
						<li><a href="#/"> Technology used <a></li>
					</ul>
				</div>
				<div class="col-sm-4 col-lg-2 mb-4 mb-lg-0 text-left">
					<h3 class="footer__title">Quick Links</h3>
					<ul class="footer__link">
						<li><a href="#/">Jobs</a></li>
						<li><a href="#/">Sponsors</a></li>
						<li><a href="#/">Partners</a></li>
						<li><a href="#/">Terms of Service</a></li>
					</ul>
				</div>
				<div class="col-sm-4 col-lg-2 mb-4 mb-lg-0 text-left">
					<h3 class="footer__title">Features</h3>
					<ul class="footer__link">
						<li><a href="#/">Current features</a></li>
						<li><a href="#/">Upcoming</a></li>
						<li><a href="#/">Suggest</a></li>
					</ul>
				</div>
				<div class="col-sm-8 col-lg-4 mb-4 mb-lg-0 text-left">
					<h3 class="footer__title">Newsletter</h3>
					<p>We don't share your data :) </p>
					<form action="" class="form-subscribe">
						<div class="input-group">
							<input type="email" class="form-control" placeholder="Your email address" required>
							<div class="input-group-append">
								<button class="btn-append" type="submit"><i class="lnr lnr-arrow-right"></i></button>
							</div>
						</div>
					</form>
				</div>
			</div>

			<div class="d-sm-flex justify-content-between footer__bottom top-border">
				<p>
					<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
					Copyright &copy;
					<script>
						document.write(new Date().getFullYear());
					</script> All rights reserved ahuzmeza uni project.
						
					<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
				</p>

			</div>

		</div>
	</footer>

	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
	<!--	<script src="vendor/bootstrap/bootstrap.bundle.min.js"></script> -->

<!-- SCRIPTS -->    
    
    <script type="text/javascript" src="js/main.js"></script>
    
</body>
</html>