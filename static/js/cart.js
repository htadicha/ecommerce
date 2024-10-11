var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
        console.log('USER:', user)


		if (user == 'AnonymousUser'){
			console.log('User is not authenticated')
			
		}else{
			updateUserOrder(productId, action)
		}


	})
}
/**
 * Sends a POST request to update the user's order with a specified product action.
 *
 * This function sends the product ID and action (e.g., add/remove) to the server via a POST request
 * using the Fetch API. The request is sent to the '/update_item/' URL, including the necessary 
 * CSRF token in the headers. After the server responds, the page is reloaded to reflect the update.
 *
 * @param {string|number} productId - The ID of the product to update.
 * @param {string} action - The action to perform on the product (e.g., 'add', 'remove').
 **/

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

/**
 * Updates the cart by adding or removing items based on user actions.
 *
 * This function modifies the cart object in the browser's cookies by either adding a new item 
 * or updating the quantity of an existing item. If the action is 'add', it increments the 
 * quantity of the specified product. If the action is 'remove', it decrements the quantity 
 * and deletes the product from the cart if the quantity reaches zero. 
 * The updated cart is then saved in a cookie and the page is reloaded to reflect changes.
 *
 * @param {string|number} productId - The ID of the product to be added or removed from the cart.
 * @param {string} action - The action to perform on the product ('add' or 'remove').
 */

function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}