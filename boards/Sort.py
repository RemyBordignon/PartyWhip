class Sort:
	def bubble_budget_descending(self, post_list):
		i = 0

		while i < len(post_list):
			j = 0

			while j < len(post_list)-i-1:
				if post_list[j].budget < post_list[j+1].budget:
					post_list[j].budget, post_list[j+1].budget = post_list[j+1].budget, post_list[j].budget
				j += 1
			i += 1

	def cocktail_budget_ascending(self, post_list):
		pass

	def selection_event_date_ascending(self, post_list):
		pass

	def insertion_event_date_descending(self, post_list):
		pass