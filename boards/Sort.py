class Sort:
	def bubble_budget_descending(self, post_list):
		i = 0

		while i < len(post_list):
			j = 0

			while j < len(post_list)-i-1:
				if post_list[j].budget < post_list[j+1].budget:
					post_list[j], post_list[j+1] = post_list[j+1], post_list[j]
				j += 1
			i += 1

	def cocktail_budget_ascending(self, post_list):
		start = 0
		end = len(post_list) - 1

		while (start < end):
			i = start

			while (i < end):
				if post_list[i].budget > post_list[i+1].budget:
					post_list[i], post_list[i+1] = post_list[i+1], post_list[i]
				i += 1

			end -= 1
			i = end

			while (i > start):
				if post_list[i].budget < post_list[i-1].budget:
					post_list[i], post_list[i-1] = post_list[i-1], post_list[i]
				i -= 1

			start += 1

	def selection_event_date_ascending(self, post_list):
		pass

	def insertion_event_date_descending(self, post_list):
		pass