\c frodex_likes;

CREATE TABLE likes
(
    post  uuid,
    likes INTEGER
);


INSERT INTO public.likes (post, likes)
VALUES ('025b89f1-cbeb-4b29-baae-0ebb476fe3d3'::uuid, 1::integer);

INSERT INTO public.likes (post, likes)
VALUES ('95d4294c-8fde-4bdc-828d-fcbb20a7de6a'::uuid, 1::integer);

INSERT INTO public.likes (post, likes)
VALUES ('5567f1a3-4611-4187-bd23-1add83cc7879'::uuid, 1::integer);

INSERT INTO public.likes (post, likes)
VALUES ('1f178e25-1047-4e8b-93ee-21c93730810f'::uuid, 1::integer);