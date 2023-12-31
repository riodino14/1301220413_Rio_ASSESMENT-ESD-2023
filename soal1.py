def analisis_rating(reviews):
    if not reviews:
        return None


    rating_terendah = min(reviews)
    rating_tertinggi = max(reviews)
    rata_rata_rating = sum(reviews) / len(reviews)


    rata_rata_rating = round(rata_rata_rating, 2)

    hasil = [rating_terendah, rating_tertinggi, rata_rata_rating]
    return hasil


data_review = [5,4,2.5,5,3.6,1.1,3.6,4,4.2,1.5]
output = analisis_rating(data_review)


print("Input:", data_review)
print("Output:", output)