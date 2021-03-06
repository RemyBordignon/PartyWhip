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
		i = 0
		while i < len(post_list):
			min_index = i

			j = i+1
			while (j < len(post_list)):
				if post_list[j].event_date < post_list[min_index].event_date:
					min_index = j
				j += 1

			post_list[i], post_list[min_index] = post_list[min_index], post_list[i]
			i += 1

	def insertion_event_date_descending(self, post_list):
		curr = 1
		while curr < len(post_list):
			post = post_list[curr]
			prev = curr - 1
			post_list[curr] = post_list[prev]

			while prev >= 0 and post_list[prev].event_date < post.event_date:
				post_list[prev + 1] = post_list[prev]
				prev -= 1

			post_list[prev + 1] = post
			curr += 1

	def insertion_pub_date_descending(self, post_list):
		curr = 1
		while curr < len(post_list):
			post = post_list[curr]
			prev = curr - 1
			post_list[curr] = post_list[prev]

			while prev >= 0 and post_list[prev].pub_date < post.pub_date:
				post_list[prev + 1] = post_list[prev]
				prev -= 1

			post_list[prev + 1] = post
			curr += 1