<?php
 error_reporting(E_ALL);
	session_start();

	$server = 'localhost';
	$user = 'root';
	$pass = '';
	$dbs = 'HoReCa';
	$errors = array(); 

// connect to the database
	$db = mysqli_connect($server, $user, $pass, $dbs);

// REGISTER USER
	if (isset($_POST['registerBtn'])) {
	  // se iau datele introduse in form la apasarea butonului 
		$first_name = mysqli_real_escape_string($db, $_POST['first_name']);
		$last_name = mysqli_real_escape_string($db, $_POST['last_name']);
		$email = mysqli_real_escape_string($db, $_POST['email']);
		$username = mysqli_real_escape_string($db, $_POST['username']);
		$password = mysqli_real_escape_string($db, $_POST['password']);

	  // verificare daca email-ul exista deja
		$email_check_query = "SELECT * FROM Administrator_Unitate WHERE email='$email' LIMIT 1";
		$result = mysqli_query($db, $email_check_query);
		$email_OK = mysqli_fetch_assoc($result);

	  // verificare daca username-ul exista deja
		$username_check_query = "SELECT * FROM Administrator_Unitate WHERE username='$username' LIMIT 1";
		$result = mysqli_query($db, $username_check_query);
		$username_OK = mysqli_fetch_assoc($result);
	  
	  //filtrare nume/prenume
		if($first_name){
			if (!preg_match("/^[a-zA-Z-' ]*$/",$first_name)) {
				array_push($errors, "În câmpul NUME, numai literele și spațiile albe sunt permise!");
			}
		} 
		if($last_name){	
			if (!preg_match("/^[a-zA-Z-' ]*$/",$last_name)) {
				array_push($errors, "În câmpul PRENUME, numai literele și spațiile albe sunt permise!");
			}
		}
		
		if ($email_OK) { 
			if ($email_OK['email'] === $email) {
			  array_push($errors, "email-ul introdus deja există!");
			}
		}

		if ($username_OK) { 
			if ($username_OK['username'] === $username) {
			  array_push($errors, "username-ul introdus deja exista!");
			}
		}
	  
	  // daca nu sunt erori in form, se face logarea
		if (count($errors) == 0) {
			$query = "INSERT INTO Administrator_Unitate (nume, prenume, email, username, parola) 
					  VALUES('$first_name', '$last_name', '$email', '$username', '$password')";
			mysqli_query($db, $query);
			$_SESSION['email'] = $email;
			$_SESSION['success'] = "Autentificat cu succes!";
			header('location:home.php');
		}
	}

// LOGIN USER
	if (isset($_POST['loginBtn'])) {
		$email = mysqli_real_escape_string($db, $_POST['email']);
		$password = mysqli_real_escape_string($db, $_POST['password']);

		if (count($errors) == 0) {
			$query = "SELECT * FROM Administrator_Unitate WHERE (email='$email' OR username='$email') AND parola='$password'";
            $get_user = mysqli_query($db, $query);
            $user = mysqli_fetch_assoc($get_user);
            $user_id = $user['id_Administrator'];
            
			if (mysqli_num_rows($user_id) == 1) {
			  $_SESSION['email'] = $email;
			  $_SESSION['id'] = $user_id;
			  $_SESSION['success'] = "Autentificat cu succes!";
			  header("location:http://localhost/HoReCa/proiect%20final/horeca.php");
			}else {
				array_push($errors, "email-ul/username-ul sau parola sunt incorecte!");
			}
		}
	}
	
// HO RE CA
	// cand se apasa pe unul dintre cele 3 butoane, sa ma redirectioneze catre categoria de inregistrare pentru unitatea respectiva

// INREGISTRARE UNITATE
	if (isset($_POST['inregistrareUnitateBtn'])) {
		// se iau datele introduse in form la apasarea butonului 
		$nume = mysqli_real_escape_string($db, $_POST['nume']);
		$descriere = mysqli_real_escape_string($db, $_POST['descriere']);
		$adresa = mysqli_real_escape_string($db, $_POST['adresa']);
		$telefon = mysqli_real_escape_string($db, $_POST['telefon']);
		$email = mysqli_real_escape_string($db, $_POST['email']);
		
		// verificare daca numele exista deja
		$name_check_query = "SELECT * FROM Unitate_HoReCa WHERE nume='$nume' LIMIT 1";
		$result = mysqli_query($db, $name_check_query);
		$nume_OK = mysqli_fetch_assoc($result);

		if ($nume_OK) { 
			if ($nume_OK['nume'] === $nume) {
			  array_push($errors, "numele introdus deja există!");
			}
		}

		//filtrare nume, telefon
		if($nume){
			if (!preg_match("/^[a-zA-Z-' ]*$/",$nume)) {
				array_push($errors, "În câmpul NUME, numai literele și spațiile albe sunt permise!");
			}
		} 
		if($telefon){
			if (!preg_match("/^[0-9]*$/", $telefon)) {
				array_push($errors, "În câmpul TELEFON, numai cifrele sunt permise!");
			}
		}

		// daca nu sunt erori in form, se face inregistrarea
		if (count($errors) == 0) {
			$tip_unitate = $_SESSION['tip_unitate'];
			$user_id = $_SESSION['id'];
			$query = "INSERT INTO Unitate_HoReCa (nume, descriere, adresa, telefon, email, cod_QR, id_Administrator, id_TipUnitate, id_Zona) 
						VALUES('$nume', '$descriere', '$adresa', '$telefon', '$email', '1', '$user_id', '$tip_unitate', '1')";
			mysqli_query($db, $query);
			header("location:http://localhost/HoReCa/proiect%20final/home.php");
		}
	}
// CRITERII




// TASK

	if (isset($_POST['addTaskBtn'])) {
		if (empty($_POST['task'])) {
			$errors = "You must fill in the task";
		}else{
			$task = $_POST['task'];
			$sql = "INSERT INTO Criterii_review (nume_Criteriu) VALUES ('$task')";
			echo "<meta http-equiv='refresh' content='0'>";
			mysqli_query($db, $sql);
		}
	}

	if (isset($_POST['deleteTaskBtn'])) {
		$id = $_GET['del_task'];
		$tip_unitate = $_SESSION['tip_unitate'];
		
		mysqli_query($db, "DELETE FROM Criterii_review WHERE id=$id");
		header("location:http://localhost/HoReCa/proiect%20final/inregistrare_unitate.php?tip_unitate=$tip_unitate");
	}
?>